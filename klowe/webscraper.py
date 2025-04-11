

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
import logging


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


def PDFtext(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        with open('name', 'wb') as fl:
            fl.write(response.content)
        text = extract_text('name')
        os.remove('name')
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


def file_to_text(file_path: str) -> list[str]:

    def html_text(file_path: str) -> list[str]:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as html:  
            soup = BeautifulSoup(html.read(), 'html.parser')
        text = soup.find_all('p')
        text = "\n".join([p.text for p in text])
        text = [j for j in [i.strip() for i in text.split("\n")] if j != ""]
        return text

    def pdf_text(file_path: str) -> list[str]:
        with open(file_path, 'rb') as pdf:  
            with open('pdf_bytes', 'wb') as fl:
                fl.write(pdf.read())
        text = extract_text('pdf_bytes').split("\n")
        text = "\n".join([i.strip() for i in text])
        text = [j for j in [i.strip() for i in text.split("\n")] if j != ""]
        os.remove('pdf_bytes')
        return text
    
    if file_path.endswith(".html"): return html_text(file_path)
    elif file_path.endswith(".pdf"): return pdf_text(file_path)
    else: raise Exception(f"Invalid file type: {file_path}. Try PDF or HTML")


###############################################################################################

