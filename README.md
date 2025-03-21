

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
> tfreq("<text>") -> list[tuple[str,int]]           == bagwords + counts tokens (types by frequency)

> count_letters("<text>") -> int                    == counts only number of letters
> count_tokens("<text>") -> int                     == counts number of tokens
> list_types("<text>") -> set[str]                  == list of unique words in a text (types)
> count_types("<text>") -> int                      == counts number of types
> typetoken_ratio("<text>") -> float                == lexical diversity as type-token ratio
> average_toklen("<text>") -> float                 == average word length (count_letters / count_tokens)
> sentence_tokenization("<text>") -> lisr[str]      == separates text by sentence
> count_sentences("<text>") -> int                  == counts number of sentences in a text
> wordsperentence("<text>") -> float                == average sentence length (count_tokens / count_sentences)
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


---


# Theory


## Linear Space
>
> Structure consisting of a set of points and the possible relaions between them.
> * **Scalar:** simple quantity expressed as a single number.
> * **Vector:** complex quantity expressed as a 1D array of numbers
> * **Matrix:** complex quantity expressed as a 2D table of numbers
> * **Tensor:** complex quantity expressed as an nD space of numbers
>
> _**Cosine Similarity**_
>> 
>
> _**Euclidean Distance**_
>> 


## Distributional Semantics
>
> Statistical semantic theory of meaning as arising from syntagmatic combinations.
> Thus, words that frequently appear in the same context must have simmilar meanings. 
>
> _**Semantic Space**_
>> In Distributional Semantics, a map of words localized according to their characteristics. Similar words would appear closer than dissimilar ones.
>
>
> _**Vector Space Model**_
>> Algebraic model of text representation based on creating its own Semantic Space where words are vectors plotted in axis naming semantic characteristics.
>> * Document: dictionary of {terms : weighted_vectors}
>> * Weight: multiplier based on importance
>
> _**Bag-of-Words**_
>> Indexing Unit Model that defines terms as an unordered weighted set of lematized words in a text after a stopwords filter.
>>
>> Term =  {bagword : weighted_vector}
>
> _**Term Frequency - Inverse Document Frequency**_
>> Weighting model based on how informative a term is in a collection of texts.
>> ``` 
>> TF.IDF = log_2( n / df(t) )
>>          {n : number of learning documents}
>>          {df(t) : number of documents where the term t appears}
>> ```


## Frame Semantics
>
> Cognitive semantic theory of meaning as tied to its associated experiential knowledge.
> Thus, any word is necessarily tied to a set of related words that encompass wordly frameworks.
>
> _**Frame**_
>> Information package about how and what to speak in a specific context. \\
>> Set of words evoqued by a given situation.
>
> _**Trigger**_
>> Discursive token that activates a cognitive semantic frame.
>
> _**Situational Frame**_
>> Set of triggers of a frame.
> 
> _**Concept**_
>> Indexing Unit Model that defines terms as an unordered weighted set of the hyperonym of each word.
>>
>> Term = normalization → {coche:sdo},{moto:sdo} → {automovil}

