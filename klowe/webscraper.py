

# klowe/webscraper.py


###############################################################################################


from .textprocessor import *
from .pythontools import *

from unidecode import unidecode
from pdfminer.high_level import extract_text
from bs4 import BeautifulSoup
import requests
import os
import operator
from operator import *
import itertools
from itertools import *


###############################################################################################


def WebPage(url: str) -> str:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        paragraphs = [p.text for p in paragraphs]
        paragraphs = " ".join(paragraphs)
        return paragraphs
    else: raise Exception(f"Not found {url = }")


def PDFtext(name: str, url: str):
    response = requests.get(url)
    if response.status_code == 200:
        with open(name, 'wb') as fl:
            fl.write(response.content)
        text = extract_text(name)
        os.remove(name)
        return text
    else: raise Exception(f"Not found {url = }")


def WikiArticle(title: str) -> str:
    lang: str = "".join(KLanguage)
    title: str = title.replace(" ", "_")
    url = f"https://{lang}.wikipedia.org/wiki/{title}"
    WT: str = WebPage(url)
    return WT


###############################################################################################


def search_engine(url: str) -> list[str]:
    lang_code = {"en":"en,en", "es":"es-ES,es", "it":"it,it", "fr":"fr,fr"}.get("".join(KLanguage))
    headers = {'Accept-Language': lang_code, 'Accept' : '*/*', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3.1 Safari/605.1.15',}
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links: list[str] = [str(i.get('href')) for i in soup.find_all('a')]
        return links
    else:
        print(f"Error: {response.status_code} in {url}")
        return [url, ]


###############################################################################################


def CleanTextFile(text: str) -> list[str]:
    text_l: list[str] = [i for i in text.split('\n')]
    # text_l: list[str] = [i for i in text_l if len(i) > 3]
    text_l: list[str] = [i for i in text_l if not contains(i, "_full_")]
    return text_l


###############################################################################################

