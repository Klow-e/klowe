

# klowe/pythontools.py


###############################################################################################


import os
import shutil
import math
import operator
from collections import Counter


###############################################################################################


def SortDict(dicc: dict) -> dict:
    sorted_d: dict = dict(sorted(dict(dicc).items(), key=operator.itemgetter(1), reverse=True))
    return sorted_d


def GetKeys(dicc: dict) -> list:
    if type(dicc) == dict:
        return list(dicc.keys())
    elif type(dicc) == list:
        return [GetKeys(i) for i in dicc]


def GetValues(dicc: dict) -> list:
    if type(dicc) == dict:
        return list(dicc.values())
    elif type(dicc) == list:
        return [GetValues(i) for i in dicc]


def CountDistribution(lista: list[str]) -> list[tuple[str,int]]:
    counter: Counter = Counter(lista)
    return counter.most_common()


def NGrams(Tok: list, n: int) -> list[tuple]:
    ngrams = [tuple(Tok[i: i + n]) for i in range(len(Tok) - n + 1)]
    return ngrams
# print(NGrams([1, 2, 3, 4, 5], 2))


###############################################################################################


def RemoveFolder(name: str) -> None:
    if os.path.exists(name):
        shutil.rmtree(name)
    if os.path.exists(f"{name}.zip"):
        os.remove(f"{name}.zip")


###############################################################################################

