

# klowe/datavisualization.py


###############################################################################################


import matplotlib.pyplot as plt


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
    plt.plot(x, y)
    plt.xticks(x, rotation=90, fontsize=8)
    plt.title("Keys distribution by Values")
    plt.xlabel("Keys")
    plt.ylabel("Values")
    plt.tight_layout()
    plt.show()
# plot_dict(Kweight_model(wiki_article("Bacilo")))


###############################################################################################

