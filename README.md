

# KlowE
```
!pip install git+https://github.com/Klow-e/klowe.git
import klowe
from klowe import *
```
You can check what can be done and how to use this package in the following Colab notebook:  
https://colab.research.google.com/drive/1JHb7EgQTV0iNRBodc7u841v6OknHrrxj?usp=sharing


## PythonTools
```
> SortDict(dict) -> dict                            == returns a sorted dict from a dict or zip item
> GetKeys(dict) -> list                             == returns a list of the keys of a dict or list of dicts
> GetValues(dict) -> list                           == returns a list of the values of a dict or list of dicts
> CountDistribution(list[str]) -> list[tuple]       == returns a count of each str in a list
> NGrams(list, n) -> list[tuple]                    == returns a list of n-grams from a list
> RemoveFolder(str)                                 == removes the folder with the given name
```


## MathStuff
```
> RandomFloat(a, b) -> float                        == gives a true random float between two floats
> RandomInt(a, b) -> int                            == gives a true random int between two ints
> RandomFloatList(a, b, length) -> list[float]      == gives a list of true random floats between two floats
> RandomIntList(a, b, length) -> list[int]          == gives a list of true random ints between two ints
> RandomWord() -> str                               == gives a pseudo-random word
> RandomWordList(length) -> list[str]               == gives a list of pseudo-random words
> RandomDictStrFloat(length) -> dict[str,float]     == gives a pseudo-random dict[str,float]

> AlKhwarizmiFunction(a, b, c, x) -> y              == solves a quadratic formula
> TanhFunction(x) -> y                              == passes data through a Tanh function
> ELU(x) -> y                                       == exponential linear unit function
> ReLU(x) -> y                                      == rectified linear unit function

> NormalizeValue(x, values, (s0, s1)) -> float      == of a value in a list of values, returns the normalized value
> NormalizeList(list[float], scale) -> list[float]  == normalizes a list of values into a (s0, s1) feature scale
> RoundList(list[float], int) -> list[float]        == rouns floats in a list to n positions
> TanhNormalization(values) -> list[float]          == normalizes values through a Tanh function, making them more extreme
> ELUNormalization(list[float])                     == passes a list of values through the ELU function
> ReLUNormalization(list[float])                    == passes a list of values through the ReLU function

> MidPoint(a, b) -> float                           == gives the midpoint between two numbers
> TopPercent(list[float], float) -> list[float]     == gets the top float per one values in a list of values
```


## WebScraper
```
> WebPage("<URL>") -> str                           == extracts somewhat clean text from an URL
> PDFtext("<URL>") -> str                           == extracts somewhat clean text from an URL to a PDF
> WikiArticle("<title>") -> str                     == extracts text from a wikipedia title
> search_engine("<URL>") -> list[str]               == extracts links in a webpage
> file_to_text(file_path: str) -> list[str]         == extracts text from a PDF or HTML file
> KWebScrap("<project>", tuple[str, ...])           == from a tuple of queries scraps the web and builds a corpus
```


## TextProcessor
```
> dirty_characters: str                             == string of characters to remove
> legal_characters: str                             == string of allowed characters in spa + ita orthography
> stop_words: list[str]                             == list of stopwords (esp + ita)

> set_language("<es>")                              == sets language for stopwords and wikipedia
> clean_text("<text>") -> str                       == normalizes text

> sentence_tokenization("<text>") -> lisr[str]      == separates text by sentence
> tokenization("<text>") -> list[str]               == clean_text + excludes tokens with illegal characters + tokenizes
> bagwords("<text>") -> list[str]                   == tokenization + stopwords filter
> list_types("<text>") -> list[str]                 == list of unique words in a text (types)

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
> DefineGrenre(list[dict]) -> dict[str,float]       == merges a list of dict[str,float] into a unified and mean-value one
> KGlossary(<model>, list[tuple[str,list[str]]])    == class that applies a weighting model to a list of (tag, texts)
> KGlossary(<model>, list).apply                    == just returns a glossary data as dict[str:[dict[str:float]]]
> sIDFw_gloss(glossary)                             == returns a glossary with sIDF * weights applied to it whole; better
> pIDFw_gloss(glossary)                             == returns a glossary with pIDF * weights applied to it whole; worse

> save_gloss(dict[str:[dict[str:float]]])           == saves glossary, like a KGlossary output, to a gloss.json file
> load_gloss()                                      == loads a gloss.json file
> example_gloss: dict[str:[dict[str:float]]]        == example of a glossary file

> KLexicon(glossary) -> dict[dict[str,np.array]]    == of a glossary type file, returns a dict with words vectorialized by genre
> print_vector("<query>", KLexicon(glossary))       == prints a single word vector with its values by genre
> VectorializeText(text, glossary, VTmodel) -> dict == returns a single textual vector from a text crosmatched with a glossary
> VTModel(g, t) -> w                                == definition of how weights are crossmatched in VectorializeText
> print_text_vector(VectorializeText())             == better way to print a text vector of a VectorializeText()
> CategorizeText(VectorializeText())                == returns two or three most likely genres with a percentage
> PrintTextGenre("<text>", glossary, VTmodel)       == directly outputs result of a categorization query

> Categorizar("<text>")                             == categorizes by topic a text in spanish
```


## ChiSquare
```
> Chi2(int, int, int) -> float                      == chi^2 test of {a, b, c} in a 2x2 contingency table (1df)
> Chi2Confidence(float) -> float                    == confidence level (per one) of a 1df chi^2

> SearchBigramUnit(str, tuple[str]) -> float        == search on a dirty text for a given bigram composition ("A", "B")
> SearchTrigramUnit(str, tuple[str]) -> float       == search on a dirty text for a given trigram composition ("A", "B", "C")

> ExtractBigramCompositions(str) -> dict[tuple,fl]  == extract from a dirty text probable bigram compositions
> ExtractTrigramCompositions(str) -> dict[tuple,fl] == extract from a dirty text probable trigram compositions
```


## DataVisualization
```
> print_dict(dict)                                  == better way to print dictionaries

> plot_dict(dict[str,float])                        == of a dict with {string:float} plots a silly little graph
> plot_function(<function>, "<name>")               == graphs a function
> plot_list(list[float])                            == graphs a list of numbers
```


---


# Theory


## Probability
>
> * **ω:** a possible world, one result of an experiment.
> * **P(ω):** probability of a particular possible world.
>     * $0 ≤ P(ω) ≤ 1 $
> * **Ω:** set of every possible world, all results of an experiment.
>     * $\sum\limits_{ω \in Ω} P(ω) = 1$
>
> _**Random Variable**_
>> A variable, or experiment, with a domain of possible result values.
>
> _**Unconditional Probability**_
>> Degree of belief in a proposition independent of other external information.
>>    * $P(a) = P(a)/A$
>>    * $P(\overline{a}) = 1 - P(a)$
>>    * $P(a) \text{ and } P(b) = P(a, b) = P(a) \cdot P(b)$
>>    * $P(a) \text{ or } P(b) = P(a) + P(b)$
>>    * $P(a) \text{ xor } P(b) = P(a + b) - P(a \cdot b)$
>
> _**Conditional Probability**_
>> Degree of belief in a proposition given already revealed evidence.
>>    * $P(a|b) = P(a \cdot b) / P(b)$
>>    * $P(\overline{a}|b) = [P(b|\overline{a}) \cdot P(\overline{a})] / P(b)$
>>
>>    * **Bayes Rule:** Knowing the probability of an effect given a cause being known, we can calculate the probability of the cause ocurring given the effect happening.
>>      * $P(b|a) = [P(a|b) \cdot P(b)] / P(a)$
>>
>>    * **Marginalization:** $P(a) = P(a, b) + P(a, \overline{b})$
>>      * $P(X = x_i) = \sum\limits_{j} P(X=x_i , Y = y_j)$
>>
>>    * **Conditioning:** $P(a) = [P(a|b) \cdot P(b)] + [P(a|\overline{b}) \cdot P(\overline{b})]$
>
> _**Probability Distribution**_
>> Table of probabilities associated with each value a variable can take.
>>    * $\mathbb{P}(\mathbb{A}) = \left< 0.6, 0.3, 0.1 \right> = $
>>      * $P(A = a_i) = 0.6$
>>      * $P(A = a_j) = 0.3$
>>      * $P(A = a_k) = 0.1$
>
> _**Joint Probability**_
>> A Probability Distribution of multiple events at once.
>>
>> |       	            | $B = b$ 	    | $B = \overline{b}$    |                       |
>> |--------------------|---------------|-----------------------|-----------------------|
>> | $A = a$ 	        | $0.08$  	    | $0.32$  	            | $a = 0.4$             |
>> | $A = \overline{a}$ | $0.02$  	    | $0.58$  	            | $\overline{a} = 0.6$  |
>> |       	            | $b = 0.1$     | $\overline{b} = 0.9$  | $1$                   |
>>
>> * $\mathbb{P}$: Probability Distribution
>> * $\mathbb{A}$: Probability Distribution of Random Variable
>> * $A$: Random Vatiable
>> * $a$: Value
>> * $\alpha$: Normalization Factor
>>
>> $\mathbb{P}(\mathbb{A}|b) = P(A, b) / P(b) = \alpha P(A, b) = \alpha \left< 0.08, 0.02\right> = \left< 0.8, 0.2\right> $
>

### Bayesian Network
>
> Data Structure that represents dependencies among Random Variables.
> Directed Graph where each node represents a Random Variable with a Probability Distribution conditioned on its Parent Nodes.
>
> * **Markov Assumption:** the current state depends only on a finite fixed number of previous states.
> * **Markov Chain:** sequence of random variables where their distributions follow the Markov Assumption.
> * **Transition Model:** Markov Chain that gives a probability of the next state based on the current state.
> * **Hidden Markov Model:** Markov Model for a system with presupposed hidden states generated by an observed event.
>
```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```


## Linear Space
>
> Structure consisting of a set of points and the possible relaions between them.
> * **Scalar:** simple quantity expressed as a single number.
> * **Vector:** complex quantity expressed as a 1D array of numbers.
> * **Matrix:** complex quantity expressed as a 2D table of numbers.
> * **Tensor:** complex quantity expressed as an nD space of numbers.
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
>>    * $TF = \sum t/d_l$
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
>

