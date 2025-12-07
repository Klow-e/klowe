

# klowe/datavisualization.py


###############################################################################################


from .pythontools import *

import matplotlib.pyplot as plt
import numpy as np


###############################################################################################


def KPrintDict(dicc: dict) -> None:
    print(p:= f"Number of items: {len(dicc)}\n\n")
    for k, v in dicc.items():
        l = len(v) if isinstance(v, (list, dict)) else len(str(v))
        print(f"{k}: \n {v} \n {l} \n\n")
    print(p)
# KPrintDict(KWeightModel(my_text))
# KPrintDict(glossary)


def KPlotDict(weighted_text: dict[str,float]) -> None:
    print(weighted_text)
    print(len(weighted_text))
    x = [i for i in weighted_text]
    y = [weighted_text.get(i) for i in weighted_text]
    plt.plot(x, y, color='black', linewidth=3)
    plt.xticks(x, rotation=90, fontsize=6)
    plt.title("Keys distribution by Values")
    plt.xlabel("Keys")
    plt.ylabel("Values")
    plt.tight_layout()
    plt.show()
    print()
# KPlotDict(RandomDictStrFloat(10))


def KPlotFunction(func: callable, name: str) -> None:
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # function
    x = np.linspace(-10, 10, 100)
    y = np.vectorize(func)(x)
    plt.plot(x, y, color='black', linewidth=3)
    plt.plot(x, x*0.333, color='black', linewidth=1)
    plt.plot(x, x, color='black', linewidth=1)
    # (0, 0)
    ax.axhline(0, color='black', linewidth=1, linestyle='--')
    ax.axvline(0, color='black', linewidth=1, linestyle='--')
    # axis borders
    ax.set_ylim(-1, 1)
    ax.set_xlim(-3, 3)
    # step size
    ax.set_xticks(np.arange(-3, 3.5, 0.5))
    ax.set_yticks(np.arange(-1, 1.5, 0.5))
    #plot
    plt.title(name, fontweight="bold")
    plt.tight_layout()
    plt.show()
# KPlotFunction(TanhFunction, "Tanh")


def KPlotList(v_list: list[float]) -> None:
    v_list.sort()
    print(v_list,"\n",len(v_list))
    ax = plt.figure().add_subplot(1, 1, 1)
    x = [str(i) for i in v_list]
    y = [i for i in v_list]
    plt.plot(x, y, color='black', linewidth=3)
    ax.axhline(max(y)/2, color='black', linewidth=1, linestyle='--')
    ax.axvline((len(y)-1)/2, color='black', linewidth=1, linestyle='--')
    plt.xticks(x, rotation=80, fontsize=6)
    plt.title("Item distribution by Values")
    plt.xlabel("Items")
    plt.ylabel("Values")
    plt.tight_layout()
    plt.show()
    print()


###############################################################################################


def print_vector(word: str, vectors):
    print("\n" + word)
    try:
        for g, v in zip(vectors.get("genres"), vectors.get("vectors").get(word)):
            print(f" {g}  \t {v}")
    except: print("Not in glossary")
    print()
# print_vector("evolucion", KLexicon(glossary))


def print_text_vector(test):
    print()
    for k, v in zip(test.get("genres"), test.get("vectors")):
        print(f"{k}:\t{v}")
    print()
# print_text_vector(VectorializeText(my_text, glossary))


###############################################################################################

