

# klowe/pythontools.py


###############################################################################################


import math
import operator


###############################################################################################


def SortDict(dicc: dict) -> dict:
    sorted_d: dict = dict(sorted(dicc.items(), key=operator.itemgetter(1), reverse=True))
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


###############################################################################################

