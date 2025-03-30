

# klowe/vectorspacemodel.py


###############################################################################################


from .textprocessor import *
from .mathstuff import *
from .pythontools import *
from .datavisualization import *
from .example_gloss import *

import nltk
from nltk import *
import math
import operator
import json
import numpy as np
np.set_printoptions(suppress=True)


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
# sample_dicts = [wiki_article("Biología"), wiki_article("Célula"), wiki_article("Carbunco"), wiki_article("Bacteria")]
# S, P, F, T = InverseDocFreq(sample_dicts)
# print("\n" + "\n\n".join("\n".join(map(str, l)) for l in [S, P, F, T]) + "\n")


def TermFreq_IDF(sample_dicts: list[str]):
    sIDF, pIDF, F_tensor, T_tensor = InverseDocFreq(sample_dicts)

    def TermFreq_IDF(IDF: list[list[float]], F_tensor: list[list[float]]):
        TF_IDF_tensor = [[IDF[i][j] * F_tensor[i][j] for j in range(len(IDF[i]))] for i in range(len(IDF))]
        return TF_IDF_tensor

    TF_sIDF = TermFreq_IDF(sIDF, F_tensor)
    TF_pIDF = TermFreq_IDF(pIDF, F_tensor)

    return TF_sIDF, TF_pIDF, T_tensor
# sample_dicts = [wiki_article("Biología"), wiki_article("Célula"), wiki_article("Carbunco"), wiki_article("Bacteria")]
# S, P, T = TermFreq_IDF(sample_dicts)
# print("\n\n".join("\n".join(map(str, l)) for l in [S, P, T]), "\n")


###############################################################################################


def KWeightModel(text: str) -> dict[str,float]:
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
        freq_dist[i] = (t, round( w * m , 10))

    weighted = SortDict(freq_dist)
    top_weighted = SortDict(zip(GetKeys(weighted), RoundList( TopPercent(GetValues(weighted), 0.35) , 10 ) ))
    return top_weighted
# print(KWeightModel(wiki_article("Bacilo")))


def DefineGenre(l_dicts: list[dict[str,float]]) -> dict[str,float]:
    all_keys: set[str] = sorted({k for d in l_dicts for k in d})
    total_d = len(l_dicts)
    genre_dict: dict = SortDict({i : (sum(d.get(i, 0) for d in l_dicts) / total_d) for i in all_keys})
    genre_dict: dict = dict(zip( genre_dict.keys() , RoundList( NormalizeList(genre_dict.values(), (0, 1)) , 10) ))
    return genre_dict
# print(DefineGenre([KWeightModel(wiki_article('Aritmética')), KWeightModel(wiki_article("Matemáticas"))]))


###############################################################################################


class KGlossary:

    def __init__(self, model: callable, gloss: list[tuple[str, list[str]]]):
        self.model = model
        #self.genres = [n for n, _ in gloss]
        #self.articles = [s for _, s in gloss]
        self.apply = {n : self.DefineGenre([self.model(d) for d in s]) for n, s in gloss}
    
    def DefineGenre(self, l_dicts: list[dict[str,float]]) -> dict[str,float]:
        return DefineGenre(l_dicts)

# glossary = KGlossary(KWeightModel, [("POLI", [wiki_article('Mao Zedong'), wiki_article('León Trotski')]),
# ("CHEM", [wiki_article('Valencia (química)'), wiki_article('Termodinámica química')]),]).apply
# print_dict(glossary)


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


def IDF_gloss(gloss: dict[str:[dict[str:float]]], xIDF: str) -> dict[str:[dict[str:float]]]:
    gd_keys: list[list[str]] = GetKeys(GetValues(gloss))
    gd_values: list[list[float]] = GetValues(GetValues(gloss))
    cor_Tdist = dict(FreqDist([j for i in gd_keys for j in i]).most_common())
    nt_tensor = [[cor_Tdist.get(j, 0) for j in i] for i in gd_keys]

    if xIDF == "sIDF":
        IDF: list[list[float]] = [[math.log2( (len(gloss) + 1) / (n + 1) ) for n in d] for d in nt_tensor]
    if xIDF == "pIDF":
        IDF: list[list[float]] = [[math.log2( ((len(gloss) - n) + 1) / (n + 1) ) for n in d] for d in nt_tensor]

    IDFw: list[list[float]] = [NormalizeList([x * y for x, y in zip(a, b)], (0,1)) for a, b in zip(IDF, gd_values)]
    IDFw: list[dict[str,float]] = [SortDict({i : j for i, j in zip(a, b) if j != 0}) for a, b in zip(gd_keys, IDFw)]

    return dict(zip(GetKeys(gloss), IDFw))


def sIDFw_gloss (gloss, xIDF = "sIDF") -> dict[str:[dict[str:float]]]:
    return IDF_gloss(gloss, xIDF)


def pIDFw_gloss (gloss, xIDF = "pIDF") -> dict[str:[dict[str:float]]]:
    return IDF_gloss(gloss, xIDF)


###############################################################################################


def KLexicon(gloss: list[dict[str:dict[str,float]]]) -> dict[str,list[str]|dict[str,np.array]]:
    all_keys: set[str] = sorted({k for i in GetKeys(GetValues(gloss)) for k in i})
    words_vectors: dict = { i : np.vstack([np.array([k]) for k in [j.get(i, 0.0) for j in GetValues(gloss)]]) for i in all_keys}
    embedded_gloss: dict = {"genres": GetKeys(gloss), "vectors": words_vectors}
    return embedded_gloss
# print_dict(KLexicon(glossary).get("vectors"))
# print(KLexicon(glossary).get("genres"))


def VTModel(g: np.array, t: float) -> np.array:
    np.set_printoptions(suppress=True)
    # w = abs( g * math.log(t) )    # works decent
    # w = ( g * TanhFunction(t) )   # works decent
    w = ( g * t )                   # works better
    return np.around(w, 8)


def VectorializeText(text: str, gloss, VTmodel: callable) -> dict[str,list]:
    vectors = KLexicon(gloss).get("vectors")
    WText: dict[str,float] = KWeightModel(text)
    WText = zip(GetKeys(WText), NormalizeList(GetValues(WText), (0, 1)))
    WText: list[list[str,float]] = [[k, v] for k, v in WText if k in vectors and v != 0]
    WText: list[list[str,float, np.array]] = [[k, v, vectors.get(k)] for k, v in WText]
    WText = {k: VTmodel(g, v) for k, v, g in WText}
    TVect = np.vstack([np.array([k]) for k in NormalizeList(sum(GetValues(WText)), (0, 1))])
    VText: dict = {"genres" : KLexicon(gloss).get("genres"), "vectors" : TVect}
    return VText
# print_dict(VectorializeText(wiki_article("Bacilo"), glossary, VTModel))


def CategorizeText(VT: dict) -> list[tuple]:
    genres = VT.get("genres")
    flat_matrix = VT.get("vectors").flatten()
    sorted_indices = np.argsort(flat_matrix)

    i_3 = sorted_indices[-3:]
    k_3 = flat_matrix[i_3]

    i_a_genre = genres[i_3[2]]
    i_b_genre = genres[i_3[1]]
    i_c_genre = genres[i_3[0]]

    i_a_trust = k_3[2] / sum(k_3)
    i_b_trust = k_3[1] / sum(k_3)
    i_c_trust = k_3[0] / sum(k_3)

    result: list[tuple] = []
    result.append((i_a_genre, i_a_trust))
    result.append((i_b_genre, i_b_trust))
    if i_c_trust >= 25:
        result.append((i_c_genre, i_c_trust))
    return result
# print(CategorizeText(VectorializeText(wiki_article("Bacilo"), glossary, VTModel)))


def PrintTextGenre(text: str, gloss, VTmodel) -> None:
    VT: dict[str,list] = VectorializeText(text, gloss, VTmodel)
    result: tuple[str,float] = CategorizeText(VT)
    print(f"Search: {text[:25]}...\n", e := "====================", "\nTopic:")
    for i in range(len(result)): print(f" {result[i][0]}: \t {result[i][1]:.0%}")
    print(e)
    print_text_vector(VT)
# PrintTextGenre(wiki_article("Bacilo"), glossary, VTModel)


###############################################################################################


def Categorizar(text: str) -> None:
    PrintTextGenre(text, example_gloss, VTModel)
# Categorizar(wiki_article("GNU"))


###############################################################################################

