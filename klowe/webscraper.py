

# klowe/webscraper.py


###############################################################################################


from .textprocessor import *

from unidecode import unidecode
from pdfminer.high_level import extract_text
from bs4 import BeautifulSoup
import requests
import os
import operator
from operator import *


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


def PDFtext(name: str, url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(name, 'wb') as fl:
            fl.write(response.content)
        text = extract_text(name)
        os.remove(name)
        return text
    else: return "not found"

#from .textprocessor import KLanguage
def wiki_article(title: str) -> str:
    lang: str = "".join(KLanguage)
    title: str = title.replace(" ", "_")
    title: str = unidecode(title)
    url = f"https://{lang}.wikipedia.org/wiki/{title}"
    WT: str = WebPage(url)
    return WT


###############################################################################################

