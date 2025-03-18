'''

###############################################################################################


import math
import operator
import numpy as np

import nltk
from nltk import *
from nltk.util import ngrams


lower_alpha = "\u03b1"
lower_chi = "\u03c7"
super_2 = "\u00b2"


###############################################################################################


import wikipedia
wikipedia.set_lang("it")

def wiki_article(title: str) -> str:
    text = wikipedia.page(title).content
    if "== Referencias ==" in text:
        text = text[ 0 : text.index("== Referencias ==")]
    if "== Note ==" in text:
        text = text[ 0 : text.index("== Note ==")]
    return text


###############################################################################################




###############################################################################################

'''