

# klowe/mathstuff.py


###############################################################################################


from .pythontools import *
from .example_gloss import *

import math
import numpy as np
import datetime
from typing import Any


###############################################################################################


def AlKhwarizmiFunction(a, b, c, x) -> float:
    y = (a * x**2) + (b*x) + c
    return round(y, 4)


def TanhFunction(x: float) -> int:
    e = 2.71828
    Tahn = ( 2 / (1 + e**(-2*x)) ) - 1
    return round(Tahn, 4)


def ELU(z: float) -> float:
    alph = 1.0
    return np.maximum(0, z) + np.minimum(0, alph * (np.exp(z) - 1))


def ReLU(x: float) -> float:
    return max(0.0, x)


###############################################################################################


def NormalizeValue(x: float, values_l: list[float], scale: tuple[float, float]) -> float:
    s0, s1 = scale
    min_v, max_v = min(values_l), max(values_l)
    dividend: float = (max_v - min_v)
    n_value: float =  ( ( (x - min_v) * (s1 - s0) ) / dividend ) + s0
    return n_value


def NormalizeList(values_l: list[float], scale: tuple[float, float]) -> list[float]:
    n_list: list[float] = [NormalizeValue(x, values_l, scale) for x in values_l]
    return n_list


def RoundList(l: list[float], n: int) -> list[float]:
    r_list: list[float] = [round(i, n) for i in l]
    return r_list


def TanhNormalization(l_values: list[float]) -> list[float]:
    l_values = NormalizeList(l_values, (-3, 3))
    TN = [TanhFunction(x) for x in l_values]
    return NormalizeList(TN, (0, 1))


def ELUNormalization(l_values: list[float]) -> list[float]:
    l_values = [ELU(x) for x in l_values]
    #l_values = NormalizeList(l_values, (0, 1))
    return l_values
# KPlotList(ELUNormalization(RandomFloatList(-1, 1, 13)))


def ReLUNormalization(l_values: list[float]) -> list[float]:
    l_values = [ReLU(x) for x in l_values]
    return l_values


def MidPoint(a: float, b: float) -> float:
    mid: float = (a * 0.5) + (b * 0.5)
    return mid


def TopPercent(values_l: list[float], threshold: float) -> list[float]:
    target_threshold: float = sum(values_l) * threshold
    sorted_values: list[float] = sorted(values_l, reverse=True)
    
    selected_v: list[float] = []
    accumulated_sum: int = 0

    for v in sorted_values:
        selected_v.append(v)
        accumulated_sum += v
        if accumulated_sum >= target_threshold:
            break
    
    return selected_v


###############################################################################################


def RandomFloat(a: float|int, b: float|int) -> float:
    """
    Gives a true random float bewteen the specified values.
    `param 1:  inclusive lower limit`
    `param 2:  inclusive upper limit`
    `returns:  a random float between those`
    `example:  random_float: float = RandomFloat(-1, 1.5)`
    """
    RSN: int = int(f"{str(datetime.datetime.now().strftime('%f')):0<6}")
    RN: float = NormalizeValue(RSN, [0, 999999], (a, b))
    return RN


def RandomInt(a: int, b: int) -> int:
    """
    Gives a true random int bewteen the specified values.
    `param 1:  inclusive lower limit`
    `param 2:  inclusive upper limit`
    `returns:  a random int between those`
    `example:  random_int: int = RandomInt(-10, 10)`
    """
    RN: int = int(RandomFloat(a, b))
    return RN


def RandomChoiceFrom(ite: Any) -> Any:
    """
    Picks a random item from an iterable.
    `param 1:  iterable object`
    `returns:  a random intem in it`
    `example:  apick: int = RandomChoiceFrom([1, 2, 3, 4])`
    """
    indexchoice: int = RandomInt(0, len(ite))
    choice = ite[indexchoice]
    return choice


def RandomIntList(a: int, b: int, l: int) -> list[int]:
    """
    Gives a list of true random ints bewteen the specified values.
    `param 1:  inclusive lower limit`
    `param 2:  inclusive upper limit`
    `param 3:  length of list`
    `returns:  a list of ints between those, length of the third param`
    `example:  random_int_list: list[int] = RandomIntList(0, 10, 8)`
    """
    RN = int(str(RandomFloat(2.7182818284, 3.1415926535))[2:]) ** 2
    RN = list(str(RN ** ((l//30)+1))[5:l+5])
    RIL = [int(i) for i in RN]
    RIL = NormalizeList(RIL, (a, b))
    RIL = [int(i) for i in RIL]
    return RIL


def RandomFloatList(a:float, b:float, l: int) -> list[float]:
    """
    Gives a list of true random floats bewteen the specified values.
    `param 1:  inclusive lower limit`
    `param 2:  inclusive upper limit`
    `param 3:  length of list`
    `returns:  a list of floats between those, length of the third param`
    `example:  random_float_list: list[float] = RandomFloatList(-1, 1, 8)`
    """
    RIL: list[float] = RandomIntList(-11, 13, l)

    RFLa: list[float] = [n for i, n in enumerate(RIL) if i % 2 == 0]
    RFLb: list[float] = [n for i, n in enumerate(RIL) if i % 2 != 0]

    RFLaa: list[float] = [n + 3.1415926535 for i, n in enumerate(RFLa) if i % 2 == 0]
    RFLab: list[float] = [n - 2.7182818284 for i, n in enumerate(RFLa) if i % 2 != 0]

    RFLba: list[float] = [n - 3.1415926535 for i, n in enumerate(RFLb) if i % 2 == 0]
    RFLbb: list[float] = [n + 2.7182818284 for i, n in enumerate(RFLb) if i % 2 != 0]

    RFL: list[float] = RFLaa + RFLbb + RFLab + RFLba
    RFL: list[float] = NormalizeList(RFL, (a, b))
    return RFL


def RandomWordList(l: int) -> list[str]:
    """
    Gives a list of pseudo-random words in Spanish.
    `param 1:  length of list`
    `returns:  a list of that length containing random words`
    `example:  random_word_list: list[str] = RandomWordList(5)`
    """
    some_keys: list[str] = list({k for i in GetKeys(GetValues(example_gloss)) for k in i[:100]})
    index: int = RandomInt(0, len(some_keys) - l)
    RSL: list[str] = [some_keys[index + i] for i in range(l)]
    return RSL


def RandomWord() -> str:
    """
    Gives a pseudo-random word in Spanish.
    `param 1:  None`
    `returns:  a random word`
    `example:  random_word: str = RandomWord()`
    """
    RS: str = "".join(RandomWordList(1))
    return RS


def RandomDictStrFloat(l: int) -> dict[str, float]:
    """
    Gives a mock dict with Spanish words as keys and random floats between 0 and 1 as values.
    `param 1:  length of dict`
    `returns:  a mock dict of words with weights between 0 and 1`
    `example:  random_dict: dict[str, float] = RandomDictStrFloat(5)`
    """
    k: list[str] = RandomWordList(l)
    v: list[float] = RandomFloatList(0, 1, l)
    RD: dict[str,float] = SortDict(dict(zip(k, v)))
    return RD


###############################################################################################

