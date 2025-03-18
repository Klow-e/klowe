

# KlowE
```
!pip install git+https://github.com/Klow-e/klowe.git
import klowe
from klowe import *
```


## Webscraping
```
> webpage(str) -> str                           == extracts somewhat clean text from an URL
> wiki_language(str)                            == sets the wikipedia language for the following code ("es", "it"...)
> wiki_article(str) -> str                      == extracts text from a wikipedia title
```


## Tokenization
```
> dirty_characters: str                         == string of characters to remove
> legal_chatacters: str                         == string of allowed characters in spa + ita orthography
> stop_words: list[str]                         == list of stopwords (esp + ita)

> clean_text("<text>") -> str                   == normalizes text
> tokenization("<text>") -> list[str]           == clean_text + excludes tokens with illegal characters + tokenizes
> bagwords(text: str) -> list[str]              == stopwords filter
> tfreq(str) -> list[tuple[str,int]]            == counts tokens
```


## ChiSquare
```
> chi2(int, int, int) -> float                  == chi^2 test of {a, b, c} in a 2x2 contingency table (1df)
> confidence_chi2(float) -> float               == confidence level (per one) of a 1df chi^2

> search_bi(str, tuple[str]) -> float           == search on a dirty text for a given bigram composition ("A", "B")
> search_tri(str, tuple[str]) -> float          == search on a dirty text for a given trigram composition ("A", "B", "C")

> extract_bicompos(str) -> dict[tuple, float]   == extract from a dirty text probable bigram compositions
> extract_tricompos(str) -> dict[tuple, float]  == extract from a dirty text probable trigram compositions
```

