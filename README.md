

# KlowE
```
!pip install git+https://github.com/Klow-e/klowe.git
import klowe
from klowe import *
```


## WebScraper
```
> webpage("<URL>") -> str                           == extracts somewhat clean text from an URL
> wiki_language("<es>")                             == sets the wikipedia language for the following code
> wiki_article("<title>") -> str                    == extracts text from a wikipedia title
```


## TextProcessor
```
> dirty_characters: str                             == string of characters to remove
> legal_chatacters: str                             == string of allowed characters in spa + ita orthography
> stop_words: list[str]                             == list of stopwords (esp + ita)

> set_language("<es>")                              == sets language for stopwords and wikipedia
> clean_text("<text>") -> str                       == normalizes text

> sentence_tokenization("<text>") -> lisr[str]      == separates text by sentence
> tokenization("<text>") -> list[str]               == clean_text + excludes tokens with illegal characters + tokenizes
> bagwords("<text>") -> list[str]                   == tokenization + stopwords filter
> list_types("<text>") -> set[str]                  == list of unique words in a text (types)

> count_letters("<text>") -> int                    == counts only number of letters
> count_tokens("<text>") -> int                     == counts number of tokens
> count_types("<text>") -> int                      == counts number of types
> count_sentences("<text>") -> int                  == counts number of sentences in a text

> typetoken_ratio("<text>") -> float                == lexical diversity as type-token ratio
> average_toklen("<text>") -> float                 == average word length (count_letters / count_tokens)
> wordspersentence("<text>") -> float               == average sentence length (count_tokens / count_sentences)

> tdistribution("<text>") -> list[tuple[str,int]]   == tokenization + counts tokens (types by frequency)
> btdistribution("<text>") -> list[tuple[str,int]]  == bagwords + counts tokens (types by frequency)
```


## VectorSpaceModel
```
> TermFrequency("<text>") -> list[tuple[str,float]] == relative frequency of each term (TF) in a text
> BagFrequency("<text>") -> list[tuple[str,float]]  == relative frequency of each bagword in a stopword-filtered text
> InverseDocFreq(list[str]) -> sIDF, pIDF, TF, T    == of a list of texts returns a list of lists for IDF, TF, and terms
> TermFreq_IDF(list[str]) -> TF_sIDF, TF_pIDF, T    == of a list of texts returns a list of lists for TF.IDF and the terms

> KWeightModel("<text>") -> dict[str, float]        == my very own weighting model for texts
> define_genre(list[dict]) -> dict[str,float]       == merges a list of dict[str,float] into a unified and mean-value one
> KGlossary(<model>, list[tuple[str,list[str]]])    == class that applies a weighting model to a list of (tag, texts)
> KGlossary(<model>, list).apply                    == just returns a glossary data as dict[str:[dict[str:float]]]
> KGlossary(<model>, list).sIDFw                    == returns a glossary with sIDF * weights applied to it whole
> KGlossary(<model>, list).pIDFw                    == returns a glossary with pIDF * weights applied to it whole

> save_gloss(dict[str:[dict[str:float]]])           == saves glossary, like a KGlossary output, to a gloss.json file
> load_gloss()                                      == loads a gloss.json file

> KLexicon(glossary) -> dict[dict[str,np.array]]    == of a glossary type file, returns a dict with words vectorialized by genre
> print_vector("<query>", KLexicon(glossary))       == prints a single word vector with its values by genre
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


## MathStuff
```
> AlKhwarizmiFunction(a, b, c, x) -> y              == solves a quadratic formula
> TanhFunction(x) -> y                              == passes data through a Tanh function
> ELU(x) -> y                                       == exponential linear unit function
> ReLU(x) -> y                                      == rectified linear unit function

> normalize_value(x, values, (s0, s1)) -> float     == of a value in a list of values, returns the normalized value
> normalize_list(list[float], scale) -> list[float] == normalizes a list of values into a (s0, s1) feature scale
> TanhNormalization(values) -> list[float]          == normalizes values through a Tanh function, making them more extreme
> ELUNormalization(list[float])                     == passes a list of values through the ELU function
> ReLUNormalization(list[float])                    == passes a list of values through the ReLU function

> midpoint(a, b) -> float                           == gives the midpoint between two numbers
> top_percent(list[float], float) -> list[float]    == gets the top float per one values in a list of values
```


## DataVisualization
```
> print_dict(dict)                                  == better way to print dictionaries

> plot_dict(dict[str,float])                        == of a dict with {string:float} plots a silly little graph
> plot_function(<function>, "<name>")               == graphs a function
> plot_list[float]                                  == graphs a list of numbers
```


## PythonTools
```
> SortDict(dict) -> dict                            == returns a sorted dict from a dict or zip item
> GetKeys(dict) -> list                             == returns a list of the keys of a dict or list of dicts
> GetValues(dict) -> list                           == returns a list of the values of a dict or list of dicts
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
> _**Vector Space Model**_
>> Algebraic model of text representation based on creating its own Semantic Space where words are vectors plotted in axis naming semantic characteristics.
>> * Document: dictionary of {terms : weighted_vectors}
>
> _**Bag-of-Words**_
>> Indexing Unit Model that defines terms as an unordered weighted set of lematized words in a text after a stopwords filter.
>>
>> Term =  {bagword : weighted_vector}
>  
> _**Weight**_
>> Multiplier for words based on relevance and entropy.
>>  
>> $t$ : term  
>> $d$ : document  
>> $d_l$ : number of tokens in a document  
>> $N$ : number of corpus documents  
>> $n_t$ : number of documents where term $t$ appears
>>  
>> * **Term Frequency:** relative frequency of a term within a document.
>>    * $TF = Σt / d_l$
>>  
>> * **Inverse Document Frequency:** meassure of how informative a term is, downweighting frequent terms. Adding $1$ to each operand is a smoothing strategy to counter division by $0$ and edge cases.
>>    * $sIDF = log_2( N + 1 / n_t + 1 )$
>>  
>> * **Probabilistic IDF:** takes into account both presence and abscense in documents.
>>    * $pIDF = log_2( N - n_t + 1 / n_t + 1)$
>>  
>> * _**Term Frequency - Inverse Document Frequency:**_ Weighting model based on how informative a term is in a collection of texts. A high weight means high frequency in the document and low frequency in other documents, thus that word would identify said document against the corpus.
>>    * $TF.IDF = TF * IDF$
>>  


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

