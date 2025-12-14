

# klowe/vectorspacemodel.py


###############################################################################################


from .textprocessor import *
from .mathstuff import *
from .pythontools import *
from .datavisualization import *
from .example_gloss import *

import math
import operator
import json
import numpy as np
np.set_printoptions(suppress=True)


###############################################################################################


def InverseDocFreq(ltexts: list[str]) -> tuple[list[list[float]], list[list[float]], list[list[float]], list[list[str]]]:
    """
    Gives the IDF of a corpus as a list of texts.
    `param 1:  list of texts`
    `return 1: smooth IDF`
    `return 2: probabilistic IDF`
    `return 3: TF of each term in each text`
    `return 4: list of the terms of each text`
    `example:  sIDF, pIDF, TFtensor, Ttensor = InverseDocFreq([texta, textb, textc])`
    """
    TF_tensor: list[list[tuple[str, int]]] = []
    T_tensor: list[list[str]] = []
    F_tensor: list[list[float]] = []

    for i in ltexts:
        # of each text
        doc_TF: list[tuple[str, float]] = TermFrequency(i)
        # list of Terms
        doc_T: list[str] = [j[0] for j in doc_TF]
        # list of T Frequencies
        doc_F: list[float] = [j[1] for j in doc_TF]
        # append to a list for each data
        TF_tensor.append(doc_TF)
        T_tensor.append(doc_T)
        F_tensor.append(doc_F)

    # dict of how many times each Term appears in the corpus as a whole
    corpus_Tdist: dict[str, int] = dict(CountDistribution([j for i in T_tensor for j in i]))
    #
    nt_tensor: list[list[int]] = [[corpus_Tdist.get(j, 0) for j in i] for i in T_tensor]
    # N: number of documents in the corpus
    corpus_N: int = len(ltexts)

    sIDF: list[list[float]] = [[math.log2((corpus_N + 1) / (nt + 1)) for nt in d] for d in nt_tensor]
    pIDF: list[list[float]] = [[math.log2(((corpus_N - nt) + 1) / (nt + 1)) for nt in d] for d in nt_tensor]
    return sIDF, pIDF, F_tensor, T_tensor


def TF_IDF(sample_dicts: list[str]):
    sIDF, pIDF, F_tensor, T_tensor = InverseDocFreq(sample_dicts)

    def TF_IDF(IDF: list[list[float]], F_tensor: list[list[float]]):
        TF_IDF_tensor = [[IDF[i][j] * F_tensor[i][j] for j in range(len(IDF[i]))] for i in range(len(IDF))]
        return TF_IDF_tensor

    TF_sIDF = TF_IDF(sIDF, F_tensor)
    TF_pIDF = TF_IDF(pIDF, F_tensor)

    return TF_sIDF, TF_pIDF, T_tensor
# sample_dicts = [my_text_bacterias, my_text_celulas, my_text_carbunco, my_text_bacilo]
# S, P, T = TF_IDF(sample_dicts)
# print("\n\n".join("\n".join(map(str, l)) for l in [S, P, T]), "\n")


###############################################################################################


def KWeightModel(text: str) -> dict[str, float]:
    freq_dist: list[tuple[str, int]] = BagFrequency(text)
    prelex_5 = {t[:5] for t, _ in freq_dist}
    prelex_6 = {t[:6] for t, _ in freq_dist}

    for i, (t, w) in enumerate(freq_dist):
        match len(t):
            case 5 | 6 | 7 : m = 1.0
            case 8 : m = 3.0
            case 4 | 9 | 10 : m = 4.0
            case 3 | _ : m = 5.0
        match True:
            case _ if t[:5] in prelex_5: m *= 4.0
            case _ if t[:6] in prelex_6: m *= 5.0
        freq_dist[i] = (t, round( w * m , 10))

    weighted: dict[str, float] = SortDict(freq_dist)
    weighted: dict[str, float] = TopPercentDict(weighted, 0.35)
    weighted: dict[str, float] = RoundDict(weighted, 10)
    return weighted

# print(KWeightModel(my_text))


def DefineGenre(l_dicts: list[dict[str, float]]) -> dict[str, float]:
    all_keys: set[str] = sorted({k for d in l_dicts for k in d})
    genre_dict: dict = SortDict({i : (sum(d.get(i, 0) for d in l_dicts) / len(l_dicts)) for i in all_keys})
    genre_dict: dict[str, float] = NormalizeDict(genre_dict, (0, 1))
    genre_dict: dict[str, float] = RoundDict(genre_dict, 10)
    return genre_dict
# print(DefineGenre([KWeightModel(my_text_aritmetica), KWeightModel(my_text_geometria)]))


###############################################################################################


class KGlossary:

    def __init__(self, model: callable, gloss: list[tuple[str, list[str]]]):
        self.model = model
        #self.genres = [n for n, _ in gloss]
        #self.articles = [s for _, s in gloss]
        self.apply = {n : self.DefineGenre([self.model(d) for d in s]) for n, s in gloss}
    
    def DefineGenre(self, l_dicts: list[dict[str, float]]) -> dict[str, float]:
        return DefineGenre(l_dicts)

# glossary = KGlossary(KWeightModel, [("POLI", [my_text_maoism, my_text_trotsky]),
# ("CHEM", [my_text_quimica, my_text_valencia]),]).apply
# KPrintDict(glossary)


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


def IDF_gloss(gloss: dict[str, dict[str, float]], xIDF: str) -> dict[str, dict[str, float]]:
    gd_keys: list[list[str]] = GetKeys(GetValues(gloss))
    gd_values: list[list[float]] = GetValues(GetValues(gloss))
    cor_Tdist = dict(CountDistribution([j for i in gd_keys for j in i]))
    nt_tensor = [[cor_Tdist.get(j, 0) for j in i] for i in gd_keys]

    if xIDF == "sIDF":
        IDF: list[list[float]] = [[math.log2( (len(gloss) + 1) / (n + 1) ) for n in d] for d in nt_tensor]
    if xIDF == "pIDF":
        IDF: list[list[float]] = [[math.log2( ((len(gloss) - n) + 1) / (n + 1) ) for n in d] for d in nt_tensor]

    IDFw: list[list[float]] = [NormalizeList([x * y for x, y in zip(a, b)], (0,1)) for a, b in zip(IDF, gd_values)]
    IDFw: list[dict[str, float]] = [SortDict({i : j for i, j in zip(a, b) if j != 0}) for a, b in zip(gd_keys, IDFw)]

    return dict(zip(GetKeys(gloss), IDFw))


def sIDFw_gloss (gloss, xIDF = "sIDF") -> dict[str:[dict[str, float]]]:
    return IDF_gloss(gloss, xIDF)


def pIDFw_gloss (gloss, xIDF = "pIDF") -> dict[str:[dict[str, float]]]:
    return IDF_gloss(gloss, xIDF)


###############################################################################################


def KLexicon(gloss: list[dict[str:dict[str,float]]]) -> dict[str,list[str]|dict[str,np.array]]:
    all_keys: set[str] = sorted({k for i in GetKeys(GetValues(gloss)) for k in i})
    words_vectors: dict = { i : np.vstack([np.array([k]) for k in [j.get(i, 0.0) for j in GetValues(gloss)]]) for i in all_keys}
    embedded_gloss: dict = {"genres": GetKeys(gloss), "vectors": words_vectors}
    return embedded_gloss
# KPrintDict(KLexicon(glossary).get("vectors"))
# print(KLexicon(glossary).get("genres"))


def VTModel(g: np.array, t: float) -> np.array:
    np.set_printoptions(suppress=True)
    # w = abs( g * math.log(t) )    # works decent
    # w = ( g * TanhFunction(t) )   # works decent
    w = ( g * t )                   # works better
    return np.around(w, 8)


def VectorializeText(text: str, gloss, VTmodel: callable) -> dict[str, list]:
    vectors = KLexicon(gloss).get("vectors")
    WText: dict[str,float] = KWeightModel(text)
    WText = zip(GetKeys(WText), NormalizeList(GetValues(WText), (0, 1)))
    WText: list[list[str,float]] = [[k, v] for k, v in WText if k in vectors and v != 0]
    WText: list[list[str,float, np.array]] = [[k, v, vectors.get(k)] for k, v in WText]
    WText = {k: VTmodel(g, v) for k, v, g in WText}
    TVect = np.vstack([np.array([k]) for k in NormalizeList(sum(GetValues(WText)), (0, 1))])
    VText: dict = {"genres" : KLexicon(gloss).get("genres"), "vectors" : TVect}
    return VText
# KPrintDict(VectorializeText(my_text, glossary, VTModel))


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
# print(CategorizeText(VectorializeText(mytext, glossary, VTModel)))


def PrintTextGenre(text: str, gloss, VTmodel) -> None:
    VT: dict[str,list] = VectorializeText(text, gloss, VTmodel)
    result: tuple[str,float] = CategorizeText(VT)
    print(f"Search: {text[:25]}...\n", e := "====================", "\nTopic:")
    for i in range(len(result)): print(f" {result[i][0]}: \t {result[i][1]:.0%}")
    print(e)
    print_text_vector(VT)
# PrintTextGenre(my_text, glossary, VTModel)


###############################################################################################


def Categorizar(text: str) -> None:
    PrintTextGenre(text, example_gloss, VTModel)
# Categorizar(my_text)


###############################################################################################

