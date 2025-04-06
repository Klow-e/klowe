

# klowe/chisquare.py


###############################################################################################


from .textprocessor import *
from .pythontools import *

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
    match chi:
        case x if 00.05 <= x < 00.10: return 0.1
        case x if 00.10 <= x < 00.15: return 0.2
        case x if 00.15 <= x < 00.25: return 0.3
        case x if 00.25 <= x < 00.40: return 0.4
        case x if 00.40 <= x < 00.60: return 0.5
        case x if 00.60 <= x < 00.90: return 0.6
        case x if 00.90 <= x < 01.10: return 0.7
        case x if 01.10 <= x < 01.15: return 0.71
        case x if 01.15 <= x < 01.20: return 0.72
        case x if 01.20 <= x < 01.25: return 0.73
        case x if 01.25 <= x < 01.30: return 0.74
        case x if 01.30 <= x < 01.40: return 0.75
        case x if 01.40 <= x < 01.45: return 0.76
        case x if 01.45 <= x < 01.50: return 0.77
        case x if 01.50 <= x < 01.55: return 0.78
        case x if 01.55 <= x < 01.65: return 0.79
        case x if 01.65 <= x < 01.70: return 0.80
        case x if 01.70 <= x < 01.80: return 0.81
        case x if 01.80 <= x < 01.85: return 0.82
        case x if 01.85 <= x < 01.95: return 0.83
        case x if 01.95 <= x < 02.05: return 0.84
        case x if 02.05 <= x < 02.15: return 0.85
        case x if 02.15 <= x < 02.25: return 0.86
        case x if 02.25 <= x < 02.40: return 0.87
        case x if 02.40 <= x < 02.50: return 0.88
        case x if 02.50 <= x < 02.65: return 0.89
        case x if 02.65 <= x < 02.80: return 0.90
        case x if 02.80 <= x < 03.00: return 0.91
        case x if 03.00 <= x < 03.20: return 0.92
        case x if 03.20 <= x < 03.45: return 0.93
        case x if 03.45 <= x < 03.70: return 0.94
        case x if 03.70 <= x < 04.05: return 0.95
        case x if 04.05 <= x < 04.25: return 0.96
        case x if 04.25 <= x < 04.30: return 0.961
        case x if 04.30 <= x < 04.35: return 0.962
        case x if 04.35 <= x < 04.40: return 0.963
        case x if 04.40 <= x < 04.45: return 0.964
        case x if 04.45 <= x < 04.50: return 0.965
        case x if 04.50 <= x < 04.55: return 0.966
        case x if 04.55 <= x < 04.60: return 0.967
        case x if 04.60 <= x < 04.65: return 0.968
        case x if 04.65 <= x < 04.70: return 0.969
        case x if 04.70 <= x < 04.75: return 0.970
        case x if 04.75 <= x < 04.80: return 0.971
        case x if 04.80 <= x < 04.90: return 0.972
        case x if 04.90 <= x < 04.95: return 0.973
        case x if 04.95 <= x < 05.00: return 0.974
        case x if 05.00 <= x < 05.10: return 0.975
        case x if 05.10 <= x < 05.15: return 0.976
        case x if 05.15 <= x < 05.25: return 0.977
        case x if 05.25 <= x < 05.30: return 0.978
        case x if 05.30 <= x < 05.40: return 0.979
        case x if 05.40 <= x < 05.50: return 0.980
        case x if 05.50 <= x < 05.55: return 0.981
        case x if 05.55 <= x < 05.65: return 0.982
        case x if 05.65 <= x < 05.75: return 0.983
        case x if 05.75 <= x < 05.90: return 0.984
        case x if 05.90 <= x < 06.00: return 0.985
        case x if 06.00 <= x < 06.15: return 0.986
        case x if 06.15 <= x < 06.25: return 0.987
        case x if 06.25 <= x < 06.40: return 0.988
        case x if 06.40 <= x < 06.55: return 0.989
        case x if 06.55 <= x < 06.75: return 0.990
        case x if 06.75 <= x < 06.95: return 0.991
        case x if 06.95 <= x < 07.15: return 0.992
        case x if 07.15 <= x < 07.45: return 0.993
        case x if 07.45 <= x < 07.75: return 0.994
        case x if 07.75 <= x < 08.10: return 0.995
        case x if 08.10 <= x < 08.55: return 0.996
        case x if 08.55 <= x < 09.15: return 0.997
        case x if 09.15 <= x < 09.60: return 0.998
        case x if 09.60 <= x < 09.70: return 0.9981
        case x if 09.70 <= x < 09.80: return 0.9982
        case x if 09.80 <= x < 09.95: return 0.9983
        case x if 09.95 <= x < 10.05: return 0.9984
        case x if 10.05 <= x < 10.15: return 0.9985
        case x if 10.15 <= x < 10.30: return 0.9986
        case x if 10.30 <= x < 10.45: return 0.9987
        case x if 10.45 <= x < 10.60: return 0.9988
        case x if 10.60 <= x < 10.75: return 0.9989
        case x if 10.75 <= x < 10.95: return 0.9990
        case x if 10.95 <= x < 11.15: return 0.9991
        case x if 11.15 <= x < 11.40: return 0.9992
        case x if 11.40 <= x < 11.65: return 0.9993
        case x if 11.65 <= x < 11.95: return 0.9994
        case x if 11.95 <= x < 12.35: return 0.9995
        case x if 12.35 <= x < 12.80: return 0.9996
        case x if 12.80 <= x < 13.45: return 0.9997
        case x if 13.45 <= x < 13.90: return 0.9998
        case x if 13.90 <= x < 14.00: return 0.99981
        case x if 14.00 <= x < 14.10: return 0.99982
        case x if 14.10 <= x < 14.20: return 0.99983
        case x if 14.20 <= x < 14.35: return 0.99984
        case x if 14.35 <= x < 14.45: return 0.99985
        case x if 14.45 <= x < 14.60: return 0.99986
        case x if 14.60 <= x < 14.75: return 0.99987
        case x if 14.75 <= x < 14.90: return 0.99988
        case x if 14.90 <= x < 15.05: return 0.99989
        case x if 15.05 <= x < 15.25: return 0.99990
        case x if 15.25 <= x < 15.45: return 0.99991
        case x if 15.45 <= x < 15.70: return 0.99992
        case x if 15.70 <= x < 16.00: return 0.99993
        case x if 16.00 <= x < 16.30: return 0.99994
        case x if 16.30 <= x < 16.65: return 0.99995
        case x if 16.65 <= x < 17.15: return 0.99996
        case x if 17.15 <= x < 17.80: return 0.99997
        case x if 17.80 <= x < 18.75: return 0.99998
        case x if 18.75 <= x < 20.85: return 0.99999
        case x if 20.85 <= x: return 1
        case _: return 0


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
    comp2 = {i : Chi2Confidence(comp2[i]) for i in comp2}
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
    comp3 = {i : Chi2Confidence(comp3[i]) for i in comp3}
    return comp3
# print(extract_tricompos("snow super white a snow super white b snow super white c snow super white d snow super white e snow super white f snow super white"))


###############################################################################################

