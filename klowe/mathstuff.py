

# klowe/mathstuff.py


###############################################################################################


from assets import gloss_example

import math
import numpy as np
import datetime


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
# v = [1.0, -0.633, -0.092, 0.226, -0.085, 0.0254, 0.358, 0.173, 0.184, 0.220, 0.119, 0.-148]
# v.sort()
# plot_list(ELUNormalization(v))


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


def RandomFloat(a:float, b:float) -> float:
    RSN: int = int(f"{str(datetime.datetime.now().strftime('%f')):0<6}")
    RN: float = NormalizeValue(RSN, [0, 999999], (a, b))
    return RN
# print(RandomFloat(0, 10))


def RandomInt(a: int, b: int) -> int:
    RN: int = int(RandomFloat(0, 10))
    return RN
# print(RandomInt(0, 10))


def RandomIntList(a:int, b:int, l: int) -> list[int]:
    RN = int(str(RandomFloat(2.7182818284, 3.1415926535))[2:]) ** 2
    RN = list(str(RN ** ((l//30)+1))[5:l+5])
    RIL = [int(i) for i in RN]
    RIL = NormalizeList(RIL, (a, b))
    RIL = [int(i) for i in RIL]
    return RIL
# print(RandomIntList(0, 10, 12))


def RandomFloatList(a:float, b:float, l: int) -> list[float]:
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
# print(RandomFloatList(0, 1, 13))


###############################################################################################

