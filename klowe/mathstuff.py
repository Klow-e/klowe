

# klowe/mathstuff.py


###############################################################################################


import math


###############################################################################################


def AlKhwarizmiFunction(a, b, c, x) -> float:
    y = (a * x**2) + (b*x) + c
    return round(y, 4)


def TanhFunction(x) -> int:
    e = 2.71828
    Tahn = ( 2 / (1 + e**(-2*x)) ) - 1
    return round(Tahn, 4)


###############################################################################################


def normalize_value(x: float, values_l: list[float], scale: tuple[float, float]) -> float:
    min_v, max_v = min(values_l), max(values_l)
    s1, s0 = scale
    n_factor: float = (s1-s0) / (max_v - min_v)
    n_value: float = (x - min_v) * n_factor
    return n_value


def normalize_list(values_l: list[float], scale: tuple[float, float]) -> list[float]:
    n_list: list[float] = [normalize_value(x, values_l, scale) for x in values_l]
    return n_list


def TahnNormalization(l_values: list[float]) -> list[float]:
    l_values = normalize_list(l_values, (5, 1))
    TN = [TanhFunction(x-3) for x in l_values]
    return normalize_list(TN, (1, 0))


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

