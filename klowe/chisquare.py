

# klowe/chisquare.py


###############################################################################################


from .tokenization import *

import scipy.stats as stats
import numoy as np
import nltk
from nltk import *
from nltk.util import ngrams
import math
import operator


###############################################################################################


def chi2(a: int, b: int, c: int) -> float:
    d = a+b+c
    chi_num = 2*d*((a*d-b*c)**2)
    chi_den = (d**2-c**2)*(d**2-b**2)
    if chi_num == 0: chi = 0
    else: chi = chi_num / chi_den
    return chi


def confidence_chi2(chi: float) -> float:
    conlvl: float = round(1-(1-stats.chi2.cdf(chi,1)), 4)
    return conlvl


###############################################################################################


def search_bi(text: str, query: tuple[str]) -> float:
    T = tokenization(text)
    bigrams = list(ngrams(T, 2))
    A = query[0]
    B = query[1]
    a: int = bigrams.count((A, B))
    b: int = T.count(A)-a
    c: int = T.count(B)-a
    chi: float = chi2(a, b, c)
    return chi
# print(search_bi(wiki_article("Semiotica"), ("la", "semiotica")))


def search_tri(text: str, query: tuple[str]) -> float:
    T = tokenization(text)
    bigrams = list(ngrams(T, 2))
    trigrams = list(ngrams(T, 3))
    A = query[0]
    B = query[1]
    C = query[2]
    a: int = trigrams.count((A, B, C))
    b: int = bigrams.count((A, B))-a
    c: int = bigrams.count((B, C))-a
    chi: float = chi2(a, b, c)
    return chi
# print(search_tri(wiki_article("Semiotica"), ("il", "segno", "e")))


def extract_bicompos(text: str) -> dict[tuple,float]:
    T = tokenization(text)
    bigrams = list(ngrams(T, 2))
    bigrams = [i for i in bigrams if i[0] not in stop_words]
    bigrams = [i for i in bigrams if i[1] not in stop_words]
    bigrams = [i for i in bigrams if i[0] != i[1]]
    alph, df, p = 0.0005, 1, 12.116
    composition2 = {}
    for i in bigrams:
        if search_bi(text, i) > p:
            composition2[i] = search_bi(text, i)
    s2 = dict(sorted(composition2.items(), key=operator.itemgetter(1), reverse=True))
    comad = [i[0] + ", " + i[1] for i in s2]
    comad = [i for i in comad if i in text]
    comad = [tuple(tokenization(i)) for i in comad]
    s2 = {i:s2[i] for i in s2 if i not in comad}
    s2 = {i:confidence_chi2(s2[i]) for i in s2}
    return s2
# print(extract_bicompos(wiki_article("Lingua greca antica")))


def extract_tricompos(text: str) -> dict[tuple, float]:
    T = tokenization(text)
    bigrams = list(ngrams(T, 2))
    trigrams = list(ngrams(T, 3))
    alph, df, p = 0.0005, 1, 12.116
    comp3 = {}
    for i in trigrams:
        if search_tri(text, i) > p:
            comp3[i] = search_tri(text, i)
    s3 = dict(sorted(comp3.items(), key=operator.itemgetter(1), reverse=True))
    s3 = {i:confidence_chi2(s3[i]) for i in s3}
    return s3
# print(extract_tricompos(wiki_article("Lingua greca antica")))


###############################################################################################

