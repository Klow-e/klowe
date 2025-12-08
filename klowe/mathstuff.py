

# klowe/mathstuff.py


###############################################################################################


from .pythontools import *
from .example_gloss import *

import math
import numpy as np
import datetime
from typing import Any
from collections.abc import Callable
from collections.abc import Sequence


###############################################################################################


def AlKhwarizmiFunction(a: float|int, b: float|int, c: float|int, x: int|float|str = '') -> float|int|Callable[[int|float], int|float]:
    """
    Of a quadratic equation in a given x solves for y.
    If y is left empty, gives a python function for f(x).
    `param 1:  a`
    `param 2:  b`
    `param 3:  c`
    `param 4:  optionally x`
    `returns:  if an x is given, then y; else, f(x)`
    `example:  yat5: float = AlKhwarizmiFunction(1, -4, -5, 5) -> 0`
    `example:  myf: Callable = AlKhwarizmiFunction(1, -4, -5) -> myf(5): float -> 0`
    """
    if type(x) != str:
        y: float|int = (a * x**2) + (b*x) + c
        return round(y, 4)
    else:
        def myf(x): return AlKhwarizmiFunction(a, b, c, x)
        return myf


def TanhFunction(x: float) -> int:
    """
    Solves y for x in the Tanh function.
    tanh(x) = (e^x - e^-x) / (e^x + e^-x)
    `param 1:  x`
    `returns:  basically 1 if positive, -1 if negative`
    `example:  tanh_atp5: float = TanhFunction(0.5)`
    """
    e = 2.71828
    Tahn = ( 2 / (1 + e**(-2*x)) ) - 1
    return round(Tahn, 4)


def ELU(z: float) -> float:
    """
    Solves y for x in the ELU function. Currently the best activation function.
    elu(x) = a * (e^x -1) if x>0, else x
    `param 1:  x`
    `returns:  x if x is positive, else aproaches -1`
    `example:  elu_atp5: float = ELU(0.5)`
    """
    alph = 1.0
    e = 2.71828
    return max(0, z) + min(0, alph * ((e**z) - 1))


def ReLU(x: float) -> float:
    """
    Solves y for x in the ReLU function.
    relu(x) = max(0,x)
    `param 1:  x`
    `returns:  x if x is positive, else 0`
    `example:  relu_atp5: float = ReLU(0.5)`
    """
    return max(0.0, x)


###############################################################################################


def NormalizeValue(x: float, values_l: list[float], scale: tuple[float, float]) -> float:
    """
    Normalizes a value in a list to a desired scale.
    `param 1:  value to be normalized`
    `param 2:  list where it would appear`
    `param 3:  tuple of the scale to normalize in`
    `returns:  aaa`
    `example:  normalized_value: float = NormalizeValue(0.314, [-0.42, -2, 2, 0.314], (0, 1))`
    """
    s0, s1 = scale
    min_v, max_v = min(values_l), max(values_l)
    dividend: float = (max_v - min_v)
    n_value: float =  ( ( (x - min_v) * (s1 - s0) ) / dividend ) + s0
    return n_value


def NormalizeList(values_l: list[float], scale: tuple[float, float]) -> list[float]:
    """
    Normalizes the values of a list[float] to a desired scale.
    `param 1:  list[float]`
    `param 2:  tuple with the lower and upper limits to normalize to`
    `returns:  the list normalized to that range`
    `example:  normalized_list: list[float] = NormalizeList([-0.42, -2, 2, 0.314], (0, 1))`
    """
    n_list: list[float] = [NormalizeValue(x, values_l, scale) for x in values_l]
    return n_list


def TanhNormalization(l_values: list[float]) -> list[float]:
    """
    Makes extreme values more extreme, scaled to (0,1)
    1: Normalizes original list to (-3,3) so the Tanh function applies equally.
    2: Passes values through a Tanh function.
    3: Normalizes result to (0,1).
    `param 1:  List of values to be normalized`
    `returns:  List through a Tanh function`
    `example:  tanh_normlis: list[float] = TanhNormalization([-3, -2. -1, 0, 1, 2, 3])`
    """
    l_values = NormalizeList(l_values, (-3, 3))
    TN = [TanhFunction(x) for x in l_values]
    return NormalizeList(TN, (0, 1))


def ELUNormalization(l_values: list[float]) -> list[float]:
    """
    1: aaaaa
    `param 1:  List of values to be normalized`
    `returns:  List through a ELU function`
    `example:  elu_normlis: list[float] = ELUNormalization([-3, -2. -1, 0, 1, 2, 3])`
    """
    l_values = [ELU(x) for x in l_values]
    return l_values


def ReLUNormalization(l_values: list[float]) -> list[float]:
    """
    1: aaaaa
    `param 1:  List of values to be normalized`
    `returns:  List through a ReLU function`
    `example:  relu_norlis: list[float] = ReLUNormalization([-3, -2. -1, 0, 1, 2, 3])`
    """
    l_values = [ReLU(x) for x in l_values]
    return l_values


###############################################################################################


def MidPoint(a: float, b: float) -> float:
    """
    Gives the number midway between two numbers.
    `param 1:  lower number`
    `param 2:  higher number`
    `returns:  midpoint between those two`
    `example:  middle_e_pi: float = MidPoint(2.7182, 3.1415)`
    """
    mid: float = (a * 0.5) + (b * 0.5)
    return mid


def TopPercent(values_l: list[float], threshold: float) -> list[float]:
    """
    Of a list of values, gives the top n perone.
    `param 1:  list of numerical values`
    `param 2:  top perone threshold`
    `returns:  values of the list that make up the top n perone of the sum of the list`
    `example:  top_30_percent_list: list[float] = TopPercent([30, 20, 20, 20, 10], 0.30)`
    """
    target_threshold: float = sum(values_l) * threshold
    sorted_values: list[float] = sorted(values_l, reverse=True)
    
    selected_v: list[float] = []
    accumulated_sum: float = 0

    for v in sorted_values:
        selected_v.append(v)
        accumulated_sum += v
        if accumulated_sum >= target_threshold:
            break
    return selected_v


def RoundList(l: list[float], n: int) -> list[float]:
    """
    Rounds every number in a list of floats to a desired size.
    `param 1:  list[float]`
    `param 2:  number of decimals to round each float`
    `returns:  the list with every float rounded to n decimals`
    `example:  rounded_list: list[float] = RoundList([-1.2077, -0.1002, 1.7261, 0.9009], 2)`
    """
    r_list: list[float] = [round(i, n) for i in l]
    return r_list


###############################################################################################


def NormalizeDict(dicc: dict[str, float], scale: tuple[float, float]) -> dict[str, float]:
    """
    Normalizes every value in a dict[str, float] to a desired size.
    `param 1:  dict[str, float]`
    `param 2:  tuple with the lower and upper limits to normalize to`
    `returns:  the dict with every value normalized to that range`
    `example:  normalized_dict: dict[str, float] = NormalizeDict({'e': 2.71, 'pi': 3.14, 'tau': 6.28}, (0, 1))`
    """
    n_dicc: dict[str, float] = {i : NormalizeValue(dicc.get(i), GetValues(dicc), scale) for i in dicc}
    return n_dicc


def RoundDict(dicc: dict[str, float], n: int) -> dict[str, float]:
    """
    Rounds every number in a dict's values to a desired size.
    `param 1:  dict[str, float]`
    `param 2:  number of decimals to round each float`
    `returns:  the dict with every value rounded to n decimals`
    `example:  rounded_dict: dict[str, float] = RoundDict({'e': 2.7182, 'pi': 3.1415, 'tau': 6.2831}, 2)`
    """
    r_dicc: dict[str, float] = {i : round(dicc[i], n) for i in dicc}
    return r_dicc


def TopPercentDict(dicc: dict[str, float], threshold: float) -> dict[str, float]:
    """
    Of a dict[str, float], gives the top n perone items based on the float values.
    `param 1:  dict of strings and floats`
    `param 2:  top perone threshold`
    `returns:  the dict but just with the items that make up the top n perone of the sum of the values`
    `example:  top_30_percent_dict: dict[str, float] = TopPercentDict({'e': 2.7182, 'pi': 3.1415, 'tau': 6.2831}, 0.30)`
    """
    sdicc: dict[str, float] = SortDict(dicc)
    target_threshold: float = sum(GetValues(dicc)) * threshold

    selected: dict[str, float] = {}
    accumulated_sum: float = 0

    for k, v in sdicc.items():
        selected.update({k:v})
        accumulated_sum += v
        if accumulated_sum >= target_threshold:
            break
    return selected


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


def RandomChoiceFrom(ite: Sequence) -> Any:
    """
    Picks a random item from an iterable.
    `param 1:  iterable object`
    `returns:  a random intem in it`
    `example:  apick: int = RandomChoiceFrom([1, 2, 3, 4])`
    """
    indexchoice: int = RandomInt(0, len(ite))
    choice: Any = ite[indexchoice]
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

