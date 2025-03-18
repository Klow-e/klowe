'''


import wikipedia
wikipedia.set_lang("it")

def wiki_article(title: str) -> str:
    text = wikipedia.page(title).content
    if "== Referencias ==" in text:
        text = text[ 0 : text.index("== Referencias ==")]
    if "== Note ==" in text:
        text = text[ 0 : text.index("== Note ==")]
    return text


'''