

# klowe/vectorspacemodel.py


###############################################################################################


from .textprocessor import *
from .mathstuff import *

import nltk
from nltk import *
from dataclasses import dataclass
import math
import operator
import json


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

# set_language("es")
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

# set_language("es")
# sample_dicts = [wiki_article("Biología"), wiki_article("Célula"), wiki_article("Carbunco"), wiki_article("Bacteria")]
# S, P, T = TermFreq_IDF(sample_dicts)
# print("\n\n".join("\n".join(map(str, l)) for l in [S, P, T]), "\n")


###############################################################################################


def Kweight_model(text: str) -> dict[str,float]:
    freq_dist: list[tuple[str,int]] = BagFrequency(text)
    prelex_5 = {t[:5] for t, _ in freq_dist}
    prelex_6 = {t[:6] for t, _ in freq_dist}

    for i, (t, w) in enumerate(freq_dist):
        match len(t):
            case x if x <= 3: m = 5.0
            case x if x <= 4: m = 4.0
            case x if x == 5: m = 1.0
            case x if x == 6: m = 1.0
            case x if x == 7: m = 1.0
            case x if x == 8: m = 3.0
            case x if x == 9: m = 4.0
            case x if x == 10: m = 4.0
            case x if x >= 11: m = 5.0
        match True:
            case _ if t[:5] in prelex_5: m *= 4.0
            case _ if t[:6] in prelex_6: m *= 5.0
        freq_dist[i] = (t, w * m)

    weighted = sorted(freq_dist, key=operator.itemgetter(1), reverse=True)
    top_w: list[float] = top_percent([w for _, w in weighted], 0.35)
    top_t: list[str] = [t for t, _ in weighted]
    top_weighted = dict(sorted(zip(top_t, top_w), key=operator.itemgetter(1), reverse=True))
    return top_weighted

# set_language("es")
# print(Kweight_model(wiki_article("Bacilo")))


çç='''
def define_genre(l_dicts: list[dict[str,float]]) -> dict[str,float]:
    all_keys: set[str] = {k for d in l_dicts for k in d}
    total_d = len(l_dicts)
    genre_dict: dict = {i : (sum(d.get(i, 0) for d in l_dicts) / total_d) for i in all_keys}
    return dict(sorted(genre_dict.items(), key=operator.itemgetter(1), reverse=True))
'''

def define_genre(l_dicts: list[dict[str,float]]) -> dict[str,float]:
    all_keys: set[str] = {k for d in l_dicts for k in d}
    total_d = len(l_dicts)
    genre_dict: dict = {i : (sum(d.get(i, 0) for d in l_dicts) / total_d) for i in all_keys}
    genre_dict: dict = dict(sorted(genre_dict.items(), key=operator.itemgetter(1), reverse=True))
    genre_dict: dict = dict(zip( genre_dict.keys() , normalize_list(genre_dict.values(), (1, 0)) ))
    return genre_dict


@dataclass
class KGlossary:
    model: callable
    genres: list[str]
    articles: list[list[str]]

    def __init__(self, model, gloss: list[tuple[str,list[str]]]) -> dict[str:[dict[str:float]]]:
        self.apply = {n : define_genre([model(d) for d in s]) for n, s in gloss}

# set_language("es")
# glossary = KGlossary(Kweight_model, [("MATH", [wiki_article('Aritmética'), wiki_article("Matemáticas")]),
# ("CHEM", [wiki_article('Valencia (química)'), wiki_article('Química')]),]).apply
# print(glossary)


def save_gloss(glossary) -> None:
    with open("gloss.json", "w") as fp:
        json.dump(glossary, fp, indent = 4)
# save_gloss(glossary)


def load_gloss():
    try:
        with open("gloss.json", "r") as fp:
            glossary = json.load(fp)
        return glossary
    except: print("No 'gloss.json' file found.")
# glossary = load_gloss()


###############################################################################################

