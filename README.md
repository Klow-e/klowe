

# KlowE
```
!pip install git+https://github.com/Klow-e/klowe.git
import klowe
from klowe import *
```

## Tokenization
```
> dirty_characters: str                  == string of characters to remove
> legal_chatacters: str                  == string of allowed characters in spa + ita orthography
> stop_words: list[str]                  == list of stopwords (esp + ita)
> clean_text("<text>") -> str            == normalizes text
> tokenization("<text>") -> list[str]    == clear_text + excludes tokens with illegal characters + tokenizes
> bagwords(text: str) -> list[str]       == stopwords filter
```

## ChiSquare
```
> chi2(int, int, int) -> float:          == chi^2 test of {a, b, c} in a 2x2 contingency table (1df)
> confidence_chi2(float) -> float:       == confidence level (per one) of a 1df chi^2
```
