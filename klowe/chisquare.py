

# klowe/chisquare.py


###############################################################################################


from .textprocessor import *
from .pythontools import *

import scipy.stats as stats
import numpy as np
import math
import operator


###############################################################################################


def Chi2(a: int, b: int, c: int) -> float:
    d = a+b+c
    chi_num = 2*d*((a*d-b*c)**2)
    chi_den = (d**2-c**2)*(d**2-b**2)
    if chi_num == 0: chi = 0
    else: chi = chi_num / chi_den
    return chi


def Chi2Confidence(chi: float) -> float:
    conlvl: float = round(1-(1-stats.chi2.cdf(chi,1)), 4)
    return conlvl


###############################################################################################


def search_bi(text: str, query: tuple[str]) -> float:
    T = tokenization(text)
    bigrams = NGrams(T, 2)
    A = query[0]
    B = query[1]
    a: int = bigrams.count((A, B))
    b: int = T.count(A)-a
    c: int = T.count(B)-a
    chi: float = Chi2(a, b, c)
    return chi
# print(search_bi("snow white a snow white b snow white c snow white d snow white e snow white f snow white", ("snow", "white")))


def search_tri(text: str, query: tuple[str]) -> float:
    T = tokenization(text)
    bigrams = NGrams(T, 2)
    trigrams = NGrams(T, 3)
    A = query[0]
    B = query[1]
    C = query[2]
    a: int = trigrams.count((A, B, C))
    b: int = bigrams.count((A, B))-a
    c: int = bigrams.count((B, C))-a
    chi: float = Chi2(a, b, c)
    return chi
# print(search_tri("snow super white a snow super white b snow super white c snow super white d snow super white e snow super white f snow super white", ("snow", "super", "white")))


def extract_bicompos(text: str) -> dict[tuple,float]:
    T = tokenization(text)
    bigrams = NGrams(T, 2)
    bigrams = [i for i in bigrams if i[0] not in stop_words]
    bigrams = [i for i in bigrams if i[1] not in stop_words]
    bigrams = [i for i in bigrams if i[0] != i[1]]
    alph, df, p = 0.0005, 1, 12.116
    comp2 = {}
    for i in bigrams:
        if search_bi(text, i) > p:
            comp2[i] = search_bi(text, i)
    comp2 = SortDict(comp2)
    comad = [i[0] + ", " + i[1] for i in comp2]
    comad = [i for i in comad if i in text]
    comad = [tuple(tokenization(i)) for i in comad]
    comp2 = {i : comp2[i] for i in comp2 if i not in comad}
    comp2 = {i : confidence_chi2(comp2[i]) for i in comp2}
    return comp2
# print(extract_bicompos("snow white a snow white b snow white c snow white d snow white e snow white f snow white"))


def extract_tricompos(text: str) -> dict[tuple, float]:
    T = tokenization(text)
    bigrams = NGrams(T, 2)
    trigrams = NGrams(T, 3)
    alph, df, p = 0.0005, 1, 12.116
    comp3 = {}
    for i in trigrams:
        if search_tri(text, i) > p:
            comp3[i] = search_tri(text, i)
    comp3 = SortDict(comp3)
    comp3 = {i : confidence_chi2(comp3[i]) for i in comp3}
    return comp3
# print(extract_tricompos("snow super white a snow super white b snow super white c snow super white d snow super white e snow super white f snow super white"))


###############################################################################################

