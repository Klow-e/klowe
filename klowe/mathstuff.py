

# klowe/mathstuff.py


###############################################################################################


import math


###############################################################################################


def normalize_value(x: float, values_l: list[float]) -> float:
    min_v, max_v = min(values_l), max(values_l)
    # 1-0 being the feature scale, to normalize values as a {0-1} range
    n_factor: float = (1-0) / (max_v - min_v)
    n_value: float = (x - min_v) * n_factor
    return n_value


def normalize_list(values_l: list[float]) -> list[float]:
    n_list: list[float] = [normalize_value(x, values_l) for x in values_l]
    return n_list


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


def AlKhwarizmiFunction(a, b, c, x) -> float:
    y = (a * x**2) + (b*x) + c
    return round(y, 4)


###############################################################################################

