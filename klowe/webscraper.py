

# klowe/webscraper.py


###############################################################################################


from bs4 import BeautifulSoup
import requests
import os
import wikipedia


###############################################################################################


def webpage(url: str) -> str:
    response=requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    paragraph=soup.find_all("p")
    output: str = ""
    for p in paragraph:
        output += p.text
        output += os.linesep
    return output


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

