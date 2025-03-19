

# KlowE
```
!pip install git+https://github.com/Klow-e/klowe.git
import klowe
from klowe import *
```


## Webscraper
```
> webpage("<URL>") -> str                           == extracts somewhat clean text from an URL
> wiki_language("<es>")                             == sets the wikipedia language for the following code
> wiki_article("<title>") -> str                    == extracts text from a wikipedia title
```


## Textprocessor
```
> dirty_characters: str                             == string of characters to remove
> legal_chatacters: str                             == string of allowed characters in spa + ita orthography
> stop_words: list[str]                             == list of stopwords (esp + ita)

> clean_text("<text>") -> str                       == normalizes text
> tokenization("<text>") -> list[str]               == clean_text + excludes tokens with illegal characters + tokenizes
> bagwords("<text>") -> list[str]                   == tokenization + stopwords filter
> tfreq("<text>") -> list[tuple[str,int]]           == bagwords + counts tokens
```


## ChiSquare
```
> chi2(int, int, int) -> float                      == chi^2 test of {a, b, c} in a 2x2 contingency table (1df)
> confidence_chi2(float) -> float                   == confidence level (per one) of a 1df chi^2

> search_bi(str, tuple[str]) -> float               == search on a dirty text for a given bigram composition ("A", "B")
> search_tri(str, tuple[str]) -> float              == search on a dirty text for a given trigram composition ("A", "B", "C")

> extract_bicompos("<text>") -> dict[tuple, float]  == extract from a dirty text probable bigram compositions
> extract_tricompos("<text>") -> dict[tuple, float] == extract from a dirty text probable trigram compositions
```

