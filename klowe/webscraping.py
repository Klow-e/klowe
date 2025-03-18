

# klowe/webscraping.py


###############################################################################################


import wikipedia
wikipedia.set_lang("it")


###############################################################################################


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

