

# klowe/vectorspacemodel.py


###############################################################################################


from .textprocessor import *
from .mathstuff import *
from .pythontools import *
from .datavisualization import *
from .example_gloss import *

from typing import NewType
import math
import operator
import json
import numpy as np
np.set_printoptions(suppress=True)


###############################################################################################


def sIDF_of_T(N: int, nt: int) -> float:
    """
    Gives the smooth IDF of an N and n_t. Same smoothing as sklearn uses.
    `formula:  sIDF = log( N+1 / nt+1 ) + 1`
    `param 1:  N: number of documents in the corpus`
    `param 2:  nt: number of documents where the term appears`
    `returns:  smooth IDF of a term in that corpus`
    `example:  sIDF_of_myterm: float = sIDF_of_T(4, 3)`
    """
    sIDF_of: float = math.log2( ((N + 1) / (nt + 1)) + 1 ) 
    return sIDF_of


def pIDF_of_T(N: int, nt: int) -> float:
    """
    Gives the probabilistic IDF of an N and n_t. The formula has also been smoothed.
    `formula:  pIDF = log( ((N - nt) + 1) / (nt + 1) )`
    `param 1:  N: number of documents in the corpus`
    `param 2:  nt: number of documents where the term appears`
    `returns:  probabilistic IDF of a term in that corpus`
    `example:  pIDF_of_myterm: float = pIDF_of_T(4, 3)`
    """
    pIDF_of: float = math.log2( ((N - nt) + 1) / (nt + 1) )
    return pIDF_of


def InverseDocFreq(ltexts: list[str]) -> tuple[list[list[float]], list[list[float]], list[list[float]], list[list[str]]]:
    """
    Gives smooth and probabilistic IDF of a list of texts corpus, alongside TF and the Terms.
    `param 1:  list of texts`
    `return1:  smooth IDF`
    `return2:  probabilistic IDF`
    `return3:  TF of each Term in each text`
    `return4:  list of the Terms of each text`
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
    # nt: list of Terms of each text with the mumber of documents where they appear
    nt_tensor: list[list[int]] = [[corpus_Tdist.get(j, 0) for j in i] for i in T_tensor]
    # N: number of documents in the corpus
    corpus_N: int = len(ltexts)
    # list with a list for each text that contains each Term's IDF
    sIDF: list[list[float]] = [[sIDF_of_T(corpus_N, nt) for nt in d] for d in nt_tensor]
    pIDF: list[list[float]] = [[pIDF_of_T(corpus_N, nt) for nt in d] for d in nt_tensor]
    return sIDF, pIDF, F_tensor, T_tensor


def TF_IDF(ltexts: list[str]) -> tuple[list[list[float]], list[list[float]], list[list[str]]]:
    """
    Gives TF.IDF, smooth and probabilistic, of a list of texts corpus, alongside the Terms.
    `param 1:  list of texts`
    `return1:  TF.sIDF`
    `return2:  TF.pIDF`
    `return3:  list of the Terms of each text`
    `example:  TFsIDF, TFpIDF, Terms = TF_IDF([texta, textb, textc])`
    """
    sIDF, pIDF, F_tensor, T_tensor = InverseDocFreq(ltexts)
    TF_sIDF: list[list[float]] = VecVecProd(sIDF, F_tensor)
    TF_pIDF: list[list[float]] = VecVecProd(pIDF, F_tensor)
    return TF_sIDF, TF_pIDF, T_tensor


###############################################################################################


def KWeightModel(text: str) -> dict[str, float]:
    """
    Weighting model for texts.
    `param 1:  text`
    `returns:  dict of relevant words with their absolute weight`
    `example:  weighted_text: dict[str, float] = KWeightModel(mytext)`
    """
    freq_dist: list[tuple[str, int]] = BagFrequency(text)
    prelex_5: set[str] = {t[:5] for t, _ in freq_dist}
    prelex_6: set[str] = {t[:6] for t, _ in freq_dist}
    # filters stopwords and applies multipliers based on length
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
    # instead of lematizing, it applies multiplier to words with popular beginnings
    weighted: dict[str, float] = SortDict(freq_dist)
    weighted: dict[str, float] = TopPercentDict(weighted, 0.35)
    return weighted


def DefineGenre(l_dicts: list[dict[str, float]]) -> dict[str, float]:
    """
    Averages the weights of every term in a list of weighted texts.
    Accounts for frequency as the weight of a term in a text where it doesn't appear is 0. 
    `param 1:  list of weighted texts as dict[str, float]`
    `returns:  dict[str, float] with every term in the list and their mean weights across the list`
    `example:  my_genre: dict[str, float] = DefineGenre([weightedtexta, weightedtextb])`
    """
    all_keys: set[str] = sorted({k for d in l_dicts for k in d})
    genre_dict: dict[str, float] = {i : (sum(d.get(i, 0) for d in l_dicts) / len(l_dicts)) for i in all_keys}
    genre_dict: dict[str, float] = SortDict(genre_dict)
    genre_dict: dict[str, float] = NormalizeDict(genre_dict, (0, 1))
    genre_dict: dict[str, float] = RoundDict(genre_dict, 10)
    return genre_dict


###############################################################################################


KGCorpusT = NewType("KGCorpusT", dict[str, list[str]])
KGlossaryT = NewType("KGlossaryT", dict[str, dict[str, float]])


def KGlossary(model: callable, gloss: KGCorpusT) -> KGlossaryT:
    """
    Applies a weighting model and 'DefineGenre()' to create a glossary datastructure that stores keywords and their weights by genre.
    `param 1:  name of a weighting function to apply, of the type 'foo(str) -> dict[str, float]'`
    `param 2:  a KGCorpusT type (dict[str, list[str]]) where the keys are genre nametags and the values lists of texts of that genre`
    `returns:  a KGlossaryT type (dict[str, dict[str, float]]) with nametags for genres and a list of weighted terms in them`
    `example:  glossary: KGlossaryT = KGlossary(KWeightModel, {"POLI": [t_maoismo, t_trotsky], "CHEM": [t_quimica, t_valencia]} )`
    """
    KGloss: KGlossaryT = {n : DefineGenre([model(d) for d in gloss[n]]) for n in gloss}
    return KGloss


def SaveKGlossary(glossary: KGlossaryT, glosspath: str = 'gloss.json') -> None:
    """
    Saves a KGlossaryT into a json file
    `param 1:  the KGlossaryT`
    `results:  'gloss.json' created`
    `example:  SaveKGlossary(myglossary)`
    """
    with open(glosspath, "w") as fp:
        json.dump(glossary, fp, indent = 4)


def LoadKGlossary(glosspath: str = 'gloss.json') -> KGlossaryT:
    """
    Loads a 'gloss.json' file.
    `returns:  the contents of a 'gloss.json' file as a KGlossaryT`
    `example:  myglossary: KGlossaryT = LoadKGlossary()`
    """
    try:
        with open(glosspath, "r") as fp:
            glossary: KGlossaryT = json.load(fp)
        return glossary
    except: print(f"No '{glosspath}' file found.")




def IDF_gloss(gloss: KGlossaryT, xIDF: str) -> KGlossaryT:
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


def PrintTextGenre(text: str, gloss, VTmodel) -> None:
    VT: dict[str,list] = VectorializeText(text, gloss, VTmodel)
    result: tuple[str,float] = CategorizeText(VT)
    print(f"Search: {text[:25]}...\n", e := "====================", "\nTopic:")
    for i in range(len(result)): print(f" {result[i][0]}: \t {result[i][1]:.0%}")
    print(e)
    print_text_vector(VT)


def Categorizar(text: str) -> None:
    PrintTextGenre(text, example_gloss, VTModel)


###############################################################################################

