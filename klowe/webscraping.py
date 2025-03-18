

# klowe/webscraping.py


###############################################################################################


import wikipedia
wikipedia.set_lang("it")


###############################################################################################


def wiki_article(title: str, lang: str) -> str:
    wikipedia.set_lang(lang)
    wikilimit: list[str] = ["== Referencias ==", "== Note ==", "== Notes et références =="]
    text = wikipedia.page(title).content
    for i in wikilimit:
        if i in text:
            text = text[ 0 : text.index(i)]
    return text


###############################################################################################

