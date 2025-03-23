

# klowe/datavisualization.py


###############################################################################################


import matplotlib.pyplot as plt
import numpy as np


###############################################################################################


def print_dict(dicc: dict):
    print(f"Dict len: {len(dicc)}")
    for k, v in dicc.items():
        print(f"\n {k}: \n {v}")
    print(f"\nDict len: {len(dicc)}")
# print_dict(Kweight_model(wiki_article("Bacilo")))


def plot_dict(weighted_text: dict[str,float]) -> None:
    print(weighted_text)
    print(len(weighted_text))
    x = [i for i in weighted_text]
    y = [weighted_text.get(i) for i in weighted_text]
    plt.plot(x, y, color='black', linewidth=3)
    plt.xticks(x, rotation=90, fontsize=8)
    plt.title("Keys distribution by Values")
    plt.xlabel("Keys")
    plt.ylabel("Values")
    plt.tight_layout()
    plt.show()
# plot_dict(Kweight_model(wiki_article("Bacilo")))


def plot_function(func: callable, name: str):
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
# plot_function(TanhFunction, "Tanh")


###############################################################################################

