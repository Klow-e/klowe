

# klowe/webscraper.py


###############################################################################################


from pdfminer.high_level import extract_text
from bs4 import BeautifulSoup
import requests
import os
import operator
from operator import *
import wikipedia


###############################################################################################


def WebPage(url: str) -> str:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        paragraphs = [p.text for p in paragraphs]
        paragraphs = " ".join(paragraphs)
        return paragraphs
    else: return "not found"


def wiki_language(lang: str):
    wikipedia.set_lang(lang)
    return(lang)

def wiki_article(title: str) -> str:
    wikilimit: list[str] = ["== Referencias ==", "== Note ==", "== Notes et références =="]
    text = wikipedia.page(title).content
    for i in wikilimit:
        if i in text:
            text = text[ 0 : text.index(i)]
    return text


###############################################################################################

