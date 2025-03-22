

# klowe/vectorspacemodel.py


###############################################################################################


from .textprocessor import *
from .mathstuff import *

import nltk
from nltk import *
import math


###############################################################################################


def TermFrequency(text: str) -> list[tuple[str,float]]:
    freq_dist: list[tuple[str,int]] = tdistribution(text)
    tokens: list[str] = [i[0] for i in freq_dist]
    doc_tlen: int = count_tokens(text)
    rel_freqs: list[float] = [i[1]/doc_tlen for i in freq_dist]
    TF: list[tuple[str,float]] = list(zip(tokens, rel_freqs))
    return TF


def BagFrequency(text: str) -> list[tuple[str,float]]:
    bfreq_dist: list[tuple[str,int]] = btdistribution(text)
    btokens: list[str] = [i[0] for i in bfreq_dist]
    doc_btlen: int = sum([i[1] for i in bfreq_dist])
    rel_freqs: list[float] = [i[1]/doc_btlen for i in bfreq_dist]
    BF: list[tuple[str,float]] = list(zip(btokens, rel_freqs))
    return BF


def InverseDocFreq(sample_dicts: list[str]):
    TF_tensor: list[list[tuple[str,int]]] = []
    T_tensor: list[list[str]] = []
    F_tensor: list[list[float]] = []

    for i in sample_dicts:

        doc_TF = TermFrequency(i)
        doc_T = [j[0] for j in doc_TF]
        doc_F = [j[1] for j in doc_TF]

        TF_tensor.append(doc_TF)
        T_tensor.append(doc_T)
        F_tensor.append(doc_F)

    cor_Tdist = dict(FreqDist([j for i in T_tensor for j in i]).most_common())
    nt_tensor = [[cor_Tdist.get(j, 0) for j in i] for i in T_tensor]
    cor_N: int = len(sample_dicts)

    sIDF = [[math.log2((cor_N + 1) / (nt + 1)) for nt in d] for d in nt_tensor]
    pIDF = [[math.log2(((cor_N - nt) + 1) / (nt + 1)) for nt in d] for d in nt_tensor]

    return sIDF, pIDF, F_tensor, T_tensor

# wiki_language("es")
# sample_dicts = [wiki_article("Biología"), wiki_article("Célula"), wiki_article("Carbunco"), wiki_article("Bacteria")]
# S, P, F, T = InverseDocFreq(sample_dicts)
# print("\n\n".join("\n".join(map(str, l)) for l in [S, P, F, T]), "\n")


def TermFreq_IDF(sample_dicts: list[str]):
    sIDF, pIDF, F_tensor, T_tensor = InverseDocFreq(sample_dicts)

    def TermFreq_IDF(IDF: list[list[float]], F_tensor: list[list[float]]):
        TF_IDF_tensor = [[IDF[i][j] * F_tensor[i][j] for j in range(len(IDF[i]))] for i in range(len(IDF))]
        return TF_IDF_tensor

    TF_sIDF = TermFreq_IDF(sIDF, F_tensor)
    TF_pIDF = TermFreq_IDF(pIDF, F_tensor)

    return TF_sIDF, TF_pIDF, T_tensor

# wiki_language("es")
# sample_dicts = [wiki_article("Biología"), wiki_article("Célula"), wiki_article("Carbunco"), wiki_article("Bacteria")]
# S, P, T = TermFreq_IDF(sample_dicts)
# print("\n\n".join("\n".join(map(str, l)) for l in [S, P, T]), "\n")


###############################################################################################


def Kweight_model(text: str) -> dict[str, float]:
    freq_dist: list[tuple[str,int]] = BagFrequency(text)
    
    for i, (t, w) in enumerate(freq_dist):

        match len(t):
            case x if x <= 3: freq_dist[i] = (t, w * 5.0)
            case x if x <= 4: freq_dist[i] = (t, w * 4.0)
            case x if x == 5: freq_dist[i] = (t, w * 1.0)
            case x if x == 6: freq_dist[i] = (t, w * 1.0)
            case x if x == 7: freq_dist[i] = (t, w * 1.0)
            case x if x == 8: freq_dist[i] = (t, w * 3.0)
            case x if x == 9: freq_dist[i] = (t, w * 4.0)
            case x if x == 10: freq_dist[i] = (t, w * 4.0)
            case x if x >= 11: freq_dist[i] = (t, w * 5.0)
        
        match True:
            case _ if t[:5] in freq_dist: freq_dist[i] = (t, w * 4.0)
            case _ if t[:6] in freq_dist: freq_dist[i] = (t, w * 5.0)

    weighted = sorted(freq_dist, key=operator.itemgetter(1), reverse=True)
    top_w: list[float] = top_percent([w for _, w in weighted], 0.30)
    top_t: list[str] = [t for t, _ in weighted]
    top_weighted = dict(sorted(zip(top_t, top_w), key=operator.itemgetter(1), reverse=True))
    return top_weighted

# print(Kweight_model(wiki_article("Bacilo")))


###############################################################################################

