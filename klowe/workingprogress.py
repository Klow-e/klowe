'''


#!pip install git+https://github.com/Klow-e/klowe.git
import klowe
from klowe import *


!pip install wikipedia
import wikipedia
wikipedia.set_lang("it")


def wiki_article(title: str) -> str:
    wikilimit: list[str] = ["== Referencias ==", "== Note ==", "== Notes et références =="]
    text = wikipedia.page(title).content
    for i in wikilimit:
        if i in text:
            text = text[ 0 : text.index(i)]
    return text


print(search_bi(wiki_article("Semiotica"), ("la", "semiotica")))
print(search_tri(wiki_article("Semiotica"), ("il", "segno", "e")))
print(extract_bicompos(wiki_article("Lingua greca antica")))
print(extract_tricompos(wiki_article("Lingua greca antica")))


'''