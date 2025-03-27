

# klowe/mathstuff.py


###############################################################################################


import math
import numpy as np


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


def normalize_value(x: float, values_l: list[float], scale: tuple[float, float]) -> float:
    s0, s1 = scale
    min_v, max_v = min(values_l), max(values_l)
    dividend: float = (max_v - min_v)
    n_value: float =  ( ( (x - min_v) * (s1 - s0) ) / dividend ) + s0
    return n_value


def normalize_list(values_l: list[float], scale: tuple[float, float]) -> list[float]:
    n_list: list[float] = [normalize_value(x, values_l, scale) for x in values_l]
    return n_list


def RoundList(l: list[float], n: int) -> list[float]:
    r_list: list[float] = [round(i, n) for i in l]
    return r_list


def TanhNormalization(l_values: list[float]) -> list[float]:
    l_values = normalize_list(l_values, (-3, 3))
    TN = [TanhFunction(x) for x in l_values]
    return normalize_list(TN, (0, 1))


def ELUNormalization(l_values: list[float]) -> list[float]:
    l_values = [ELU(x) for x in l_values]
    #l_values = normalize_list(l_values, (0, 1))
    return l_values
# v = [1.0, -0.633, -0.092, 0.226, -0.085, 0.0254, 0.358, 0.173, 0.184, 0.220, 0.119, 0.-148]
# v.sort()
# plot_list(ELUNormalization(v))


def ReLUNormalization(l_values: list[float]) -> list[float]:
    l_values = [ReLU(x) for x in l_values]
    return l_values


def midpoint(a: float, b: float) -> float:
    mid: float = (a * 0.5) + (b * 0.5)
    return mid


def top_percent(values_l: list[float], threshold: float) -> list[float]:
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

