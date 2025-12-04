

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
> search_engine("<URL>") -> list[str]               == extracts links in a webpage
> file_to_text(file_path: str) -> list[str]         == extracts text from a PDF or HTML file
> KWebScrap("<project>", tuple[str, ...])           == from a tuple of queries scraps the web and builds a corpus
```


## TextProcessor
```
> dirty_characters: str                             == string of characters to remove
> legal_characters: str                             == string of allowed characters in spa + ita orthography
> stop_words: list[str]                             == list of stopwords (esp + ita)

> set_language("<es>")                              == sets language for stopwords and webpages
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


## Arithmetics
>
> Science of quantities and their operations.
>
> * **Quantity:** anything admitting of increasing or decreasing.
>    * **Continious:** cannot be segmented.
>        * **Nominal:** unordered categories without distance, like colors.
>        * **Ordinal:** ordered undivisible ranking, like lists.
>    * **Discrete:** consisting of segmentable parts.
>        * **Interval:** data with relative divisible distances, like temperature.
>        * **Ratio:** cardinal count with true zero, like volume.
> * **Measure:** comparing a Quantity to another known one of the same kind.
> * **Unit:** base Quantity used to Meassure others of its kind.
> * **Complex Number:** multi-dimensional Quantity not representable by just one Number at once.
> * **Real Number:** representation of a Quantity as relation to the Unit.
>    * **Transcendental:** not obtainable by Polynomial Equations, like $e$.
>        * **Uncomputable:** not obtainable by Computation, like $\Omega$.
>        * **Computable:** obtainable by Algorithmic Computation, like $e$.
>    * **Algebraic:** obtainable by Polynomial Equations, like $\sqrt[3]{2}$.
>        * **Constructable:** obtainable in a Cartesian Plane, like $\sqrt{2} $.
>        * **Rational:** ratios to the Unit, like $\frac{5}{4}$.
>        * **Integerns:** obtainable by stacking or removing Units, like $-3$.
>        * **Whole:** obtainable by stacking Units or its absence, like $0$.
>        * **Natural:** obtainable by stacking Units, like $2$.
>

### Linear Programming
> 
> Algebraic technique for optimizing a Cost Function subject to Constraints.
>
> * $b_l \leq \sum\limits_{i} (a_i \cdot x_i) \leq b_u$
>
> Example:
> * Cost Function: $50x_1 + 80x_2$
> * Constraint: $5x_1 + 2x_2 \leq 20$
> * Constraint: $[10x_1 + 12x_2 \geq 90] \cdot -1\implies (-10x_1) + (-12x_2) \leq -90$
>
> _**Constraint Satisfaction**_
>>
>> * **Set of Variables:** $V\{x_1, x_2, x_3, ...\}$
>> * **Set of their Domains:** $D\{d_1, d_2, d_3, ...\}$
>> * **Set of Constraints:** $C\{c_a, c_b, c_c, ...\}$
>>    * **Soft Constraints:** preferable.
>>    * **Hard Constraints:** obligatory.
>>    * **Unary Constraint:** involves just one Variable. $\{A \neq 1\}$
>>        * **Node Consistency:** all Values in a Variable's Domain satisfy its Unary Constraints.
>>    * **Binary Constraint:** involves just two Variables. $\{A \neq B\}$
>>        * **Arc Consistency:** All Values in a Variable's Domain satisfy its Binary Constraints.
>>
>> Example: Sudoku
>> * $V: \{(0,2), (1,1), (1,2), ... \}$
>> * $D: V\{0-9\}$
>> * $C: \{(0,2) \neq (1,1) \neq (1,2), ... \}$
>>
>> Example: Date
>> * $V_D: A\{Mon, Tue, Wed\} ; B\{Mon, Tue, Wed\}$
>> * $C: \{A \neq Mon, B \neq Tue, B \neq Mon, A \neq B \}$
>> * Node Consistency: $A\{Tue, Wed\} ; B\{Wed\}$
>> * Arc Consistency: $A\{Tue\} ; B\{Wed\}$
>

### Linear Space
>
> Structure consisting of a set of points and the possible relaions between them.
>
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
>


## Probability
>
>
>
> * $ω$: a possible world, one result of an experiment.
> * $P(ω)$: probability of a particular possible world.
>     * $0 ≤ P(ω) ≤ 1 $
> * $Ω$: set of every possible world, all results of an experiment.
>     * $\sum\limits_{ω \in Ω} P(ω) = 1$
>
> _**Random Variable**_
>> A variable, or experiment, with a domain of possible result values.
>
> _**Unconditional Probability**_
>> Degree of belief in a proposition independent of other external information.
>>    * $P(a) = \frac{P(a)}{A}$
>>    * $P(\overline{a}) = 1 - P(a)$
>>    * $P(a) \text{ and } P(b) = P(a, b) = P(a) \cdot P(b)$
>>    * $P(a) \text{ or } P(b) = P(a) + P(b)$
>>    * $P(a) \text{ xor } P(b) = P(a + b) - P(a \cdot b)$
>
> _**Conditional Probability**_
>> Degree of belief in a proposition given already revealed evidence.
>>    * $P(a|b) = P(a \cdot b) / P(b)$
>>    * $P(\overline{a}|b) = \frac{P(b|\overline{a}) \cdot P(\overline{a})}{P(b)}$
>>
>>    * **Bayes Rule:** Knowing the probability of an effect given a cause being known, we can calculate the probability of the cause ocurring given the effect happening.
>>      * $P(b|a) = \frac{P(a|b) \cdot P(b)}{P(a)}$
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
>> * $A$: Random Variable
>> * $a$: Value
>> * $\alpha$: Normalization Factor
>>
>> $\mathbb{P}(\mathbb{A}|b) = \frac{P(A, b)}{P(b)} = \alpha P(A, b) = \alpha \left< 0.08, 0.02\right> = \left< 0.8, 0.2\right> $
>

## Bayesian Network
>
> Data Structure that represents dependencies among Random Variables.
> Markov Chain where each node represents a Random Variable with a Probability Distribution conditioned on its Parent Nodes.
>
> ```mermaid
> graph TD;
>       A["𝔸 {a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>}"]
>       B["𝔹 {b, b̅}"]
>       C["ℂ {c, c̅}"]
>       D["𝔻 {d, d̅}"]
>
>       A-->B;
>       B-->C;
>       A-->C;
>       C-->D;
> ```
>
> | $a_1$     | $a_2$ | $a_3$ | $\mathbb{A}$  |
> |-----------|-------|-------|---------------|
> | $0.7$     | $0.2$ | $0.1$ | 1             |
>
> | $\mathbb{A}$                | $b$       | $\overline{b}$| $\mathbb{B}$  |
> |-----------------------------|-----------|---------------|---------------|
> | $a_1$                       | $0.4$     | $0.6$         | 1             |
> | $a_2$                       | $0.2$     | $0.8$         | 1             |
> | $a_3$                       | $0.1$     | $0.9$         | 1             |
>
> | $\mathbb{A}$| $\mathbb{B}$  | $c$       | $\overline{c}$| $\mathbb{C}$  |
> |-------------|---------------|-----------|---------------|---------------|
> | $a_1$       | $b$           | $0.8$     | $0.2$         | 1             |
> | $a_1$       | $\overline{b}$| $0.9$     | $0.1$         | 1             |
> | $a_2$       | $b$           | $0.8$     | $0.4$         | 1             |
> | $a_2$       | $\overline{b}$| $0.7$     | $0.3$         | 1             |
> | $a_3$       | $b$           | $0.4$     | $0.6$         | 1             |
> | $a_3$       | $\overline{b}$| $0.5$     | $0.5$         | 1             |
>
> | $\mathbb{C}$                | $d$       | $\overline{d}$| $\mathbb{D}$  |
> |-----------------------------|-----------|---------------|---------------|
> | $c$                         | $0.9$     | $0.1$         | 1             |
> | $\overline{c}$              | $0.6$     | $0.4$         | 1             |
>
> * $P(a_2, \overline{b}) = P(a_2) \cdot P(\overline{b}|a_2)$
>
> * $P(a_2, \overline{b}, \overline{c}) = P(a_2) \cdot P(\overline{b}|a_2) \cdot P(\overline{c}|a_2,\overline{b})$
>
> * $P(a_2, \overline{b}, \overline{c}, d) = P(a_2) \cdot P(\overline{b}|a_2) \cdot P(\overline{c}|a_2,\overline{b}) \cdot P(d|\overline{c})$
>
> * $\mathbb{P}(\mathbb{D}|a_2,\overline{b}) = \alpha \mathbb{P}(\mathbb{D}, a_2, \overline{b}) = \alpha [\mathbb{P}(\mathbb{D}, a_2, \overline{b}, c) + \mathbb{P}(\mathbb{D}, a_2, \overline{b}, \overline{c})]$
>
> _**Inference by Enumeration**_
>> $\mathbb{P}(\mathbb{X}|e) = \alpha \mathbb{P}(\mathbb{X},e) = \alpha \sum\limits_{y} P(X, e, y)$
>> * $\mathbb{X}$: query variable for which to compute distribution.
>> * $E$: observed variable of an event.
>> * $e$: evidence value for $E$
>> * $Y$: non-evidence non-query hidden variables.
>
> _**Rejection Sampling**_
>> Of a Bayesian Network, picking a bunch of sample queries and using it as a probabilistic model.
>> * The result for a simple query would be in how many of the samples is the query present.
>> * The result of a conditional query would be of the samples where the condition is met, in how many is the query present.
>

### Chi-Squared Distribution
>
> Statistical distribution of a Contingency Table of Random Variables.
>
> * **Null Hypothesis:** Assumption that a given distribution of two Variables can perfectly be explained by probabilistic chance alone.
>     * $H_0: P(A|B) = P(A|\overline{B})$
> * **P-Value:** probability of obtaining a given result or a more extreme one under the Null Hypothesis.
>     * $p = P[x \leq \chi^2]$
> * **Significance Level:** degree of certainty in rejecting the Null Hypothesis.
>     * $p \leq \alpha \implies \overline{H_0}$
> * **Degrees of Freedom:** Description of the parameters of an $M \cdot N$ Contingency Table necessary for Chi-Squared calculations.
>     * $d.f. = (M-1) \cdot (N-1)$
>
> _**Contingency Table**_
>> Joint Probability table used in Statistics to plot probabilities of events.
>>
>> * $a$: the event $A$ happens.
>> * $\overline{a}$: the event $A$ doesn't happen.
>> * $α$: total times $A$ and $B$ happen together.
>> * $β$: times $A$ happens without $B$ happening.
>> * $(α+β)$: total times $A$ happens.
>> * $(γ+δ)$: total times $A$ doesn't happen.
>> * $N$: total number of things that can happen.
>>
>> | $df = 1$              | $B = b$ 	           | $B = \overline{b}$    |            |
>> |-----------------------|-----------------------|-----------------------|------------|
>> | $A = a$ 	           | $α_{ab} $  	       | $β_{a\overline{b}}$   | $(α+β)$    |
>> | $A = \overline{a}$    | $γ_{\overline{a}b}$   | $δ_{\overline{ab}}$   | $(γ+δ)$    |
>> |       	               | $(α+γ)$               | $(β+δ)$               | $N$        |
>>
>> * $a = (α+β)$
>> * $\overline{a} = (γ+δ)$
>> * $b = (α+γ)$ 
>> * $\overline{b} = (β+δ)$
>> * $N = α+β+γ+δ$
>> * $δ = N-α-β-γ$
>
> _**Chi-Squared Test**_
>>
>> Test to (dis)prove the Null Hypothesis, determining how probable it is that two events occur simultaneously by chance alone.
>> To disprove the Null Hypothesis means to conclude that the distribution of two simultaneous events is not explicable by pure chance, but are conditioned.
>>
>> * $\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$
>>
>>    * $O_i$: observed values in the Contingency Table.
>>
>>    * $E_i$: expected values assuming the Null Hypothesis
>>
>> * $\chi^2_{(df=1)} = \frac{α-E_α}{E_α} + \frac{β-E_β}{E_β} + \frac{γ-E_γ}{E_γ} + \frac{δ-E_δ}{E_δ} = \frac{(α+β+γ+δ)(αδ-βγ)^2}{(α+β)(γ+δ)(α+γ)(β+δ)}$
>>
>>    * $E_α = \frac{(α+β)(α+γ)}{N}$
>>
>>    * $E_β = \frac{(α+β)(β+δ)}{N}$
>>
>>    * $E_γ = \frac{(γ+δ)(α+γ)}{N}$
>>
>>    * $E_δ = \frac{(γ+δ)(β+δ)}{N}$
>


## Artificial Intelligence
>
>
>
> * **Machine Learning:** techniques to make a program learn from data without explicit instructions.
>
> * **Agent:** entity that percives and acts upon its enviroment.
>
> * **State:** A particular configuration of the Agent in its enviroment.
>
> * **Initial State:** the State from where the Agent begins.
>
> * **Goal State:** desired final State.
>
> _**Markov Model**_
>>
>> * **Markov Assumption:** the current state depends only on a finite fixed number of previous states.
>>
>> * **Markov Chain:** sequence of random variables where their distributions follow the Markov Assumption.
>>
>> * **Transition Model:** Markov Chain that gives a probability of the next state based on the current state.
>>
>> * **Hidden Markov Model:** Markov Model for a system with presupposed hidden states generated by an observed event.
>>
>> * **Markov Decission Process:** Markov Model for decisions, states, actions, and rewards.
>

### Supervised Machine Learning
>
> Based on a set of inputs to outputs, map new inputs to outputs.
>
> * **Classification:** divides data into binary classes.
>
> * **Regression:** predicts the value of an input.
>
> _**Nearest Neighbour Classifier**_
>> a
>
> _**K-Nearest Neighbour Classifier**_
>> a
>
> _**Support Vector Machine Classifier**_
>> a
>
> _**Random Forest Classifier**_
>> a
>  
> _**Naive Bayes Classifier**_
>> a
>
> _**Linear Regression**_
>> a
>
> _**Logistic Regression**_
>> a
>
> _**Random Forest Regression**_
>> a
>


### Reinforcement Machine Learning
>
> Based on a set of rewards or punishments, learn the optimal actions.
>
> ```mermaid
> graph LR;
>       A(Enviroment)
>       B(Agent)
>
>       A-->|reward|B;
>       A-->|state|B;
>       B-->|action|A;
> ```
>
>

### Unsupervised Machine Learning
>
> Learning patterns alone without any aditional feedback.
>
> _**K-Means Clustering**_
>>
>

### Neural Network
>
> Machine Learning non-linear function based on interconnected nodes.
>
> * $M$: size of training set.
>
> * $n$: ammount of input variables.
>
> * $L$: ammount of layers.
>
> * $l$: specific layer.
>
> * $W^l$: weights for layer $l$.
>
> * $b^l$: bias for layer $l$.
>
> * $x_i$: single input variable.
>


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
>>    * $TF = \sum \frac{t}{d_l}$
>>    
>> * **Inverse Document Frequency:** meassure of how informative a term is, downweighting frequent terms. Adding $1$ to each operand is a smoothing strategy to counter division by $0$ and edge cases.
>>    * $sIDF = log_2(\frac{N + 1}{n_t + 1})$
>>  
>> * **Probabilistic IDF:** takes into account both presence and abscense in documents.
>>    * $pIDF = log_2(\frac{N - n_t + 1}{n_t + 1})$
>>  
>> * _**Term Frequency - Inverse Document Frequency:**_ Weighting model based on how informative a term is in a collection of texts. A high weight means high frequency in the document and low frequency in other documents, thus that word would identify said document against the corpus.
>>    * $TF.IDF = TF * IDF$
>


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


## Generativism
>
> Linguistic school derived from Northamerican Structuralism as a response to Behaviourism, placing linguistics inside of psychology.
>
> * **Grammar:** recursive rule system that generates sentences.
>
> * **Economic Efficiency:** models should be the smaller they can be.
>
> * **Universalism:** models should be general with principles for all languages.
>
> * **Competence:** idealized speaker's unconscious knowledge about their language that ables them to comprehend an infinite amount sentences and distinguish grammaticality.
>    * **Error:** lack of the speaker's Competence.
>
> * **Performance:** specific realization of a Competence.
>    * **Failure:** due to external factors.
>
> _**(TGG) Transformational-Generative Grammar**_
>> A generative formal system as description for natural language.
>> * **(50's, CT) Classical Theory:**
>>    * Phrase Structure Rules
>>    * Transformation Rules
>>    * Deep/Surface Structure
>> * **(60's, ST) Standard Theory:**
>>    * Lexical Insertion Rules
>>    * Subcategorization
>>    * Semantic Interpretation
>>    * Competence/Performance
>> * **(70's, EST) Extended Standard Theory:**
>>    * Trace Theory
>>    * Constraints
>> * **(80's, GB) Goberment and Binding Theory:**
>>    * ~~Rules~~ $\rightarrow$ Principles & Parameters
>>    * P&P Modules:
>>        * X-bar Theory
>>        * Theta Theory
>>        * Case Theory
>>        * Binding Theory
>>        * Bounding Theory
>>        * Control Theory
>>        * Goberment
>> * **(90's, MP) Minimalist Program:**
>>    * ~~Principles & Parameters~~ $\rightarrow$ Core Operations:
>>        * Merge
>>        * Move
>>        * Agree
>>    * ~~X-bar Theory~~ $\rightarrow$ Bare Phrase Structure
>>    * ~~Goverment~~ $\rightarrow$ Feature-Checking
>>    * ~~Deep/Surface Structure~~ $\rightarrow$ Derivation
>
> _**(CFG) Context-Free Grammar**_
>>
>> A constituency formal system of combination/grouping rules and a lexicon that generate possible sentences.
>>
>> * **Phrase Structure Rules:** generation rules for non-terminal nodes.
>>
>> * **Lexion:** terminal nodes set of equivalences.
>>
>> * **Lexicalized CFG:** a CFG that relies more on the Lexicon rather than the Phrase Structure Rules.
>>    * (LFG) Lexical-Functional Grammar
>>    * (HPSG) Head-Driven Phrase Structure Grammar
>>    * (TAG) Tree-Adjoining Grammar
>>    * (CCG) Combinatory Categorical Grammar
>>
>> * **Derivation:** expanding the rules to generate a terminal set of strings.
>>    * $NP \rightarrow Det + N \rightarrow \text{a cat}$
>>
>> * **Parse Tree:** graphical representation of a derivation.
>>
>> * **Bracket Notation:** bracketed representation of a derivation.
>>
>> * **Grammaticality:** property of a string that can be derived from a grammar.
>>
>> * **Grammar:** $G_{CFG} = (S, N, \Sigma, R)$
>>    * $S$: start symbol, top node of a parse tree $\{S\}$.
>>    * $N$: set of non-terminal symbols, for the rules symbols $\{A, B, C,...\}$.
>>    * $\Sigma$: set of terminal symbols, for the lexicon symbols $\{a, b, c,...\}$.
>>    * $R$: set of production rules as $A \rightarrow \beta$:
>>        * $A \in N$
>>        * $\beta \in (\Sigma \cup N)* $
>>
>> * **Language:** a set of strings derivable from the designated Start Symbol.
>>    * $\mathscr{L}_G = \{w \in \Sigma^* : S \Rightarrow^* w\}$
>>
>> * **English Phrase Structure Rules:**
>>```
>>
>>  S      ->     NP    +   (AUX) +   VP
>>
>>
>>  AUX    ->     do
>>         |      do    +   have
>>         |      do    +   be
>>         |      do    +   M
>>         |      M
>>
>>  M      ->     { can | may | must | shall | will }
>>         |      M     +   have
>>         |      M     +   be
>>
>>
>>  NP     ->     Nom
>>         |      Det   +   Nom
>>         |      Det   +   PP
>>
>>  Det    ->     { the | a | this | my | any | one | ... }
>>         |      NP-'s
>>
>>  Nom    ->     N
>>         |      AP*   +   N
>>         |      N     +   PP*
>>         |      AP*   +   N     +   PP*
>>         |      Nom   +   GerVP
>>         |      Nom   +   RelC
>>
>>  N      ->     { rose | solitude | god | sun | ... }
>>
>>  RelC   ->     { who | that }  +   VP   
>>
>>  GerVP  ->     GerV  
>>         |      GerV  +   NP
>>         |      GerV  +   PP
>>         |      GerV  +   NP    +   VP
>>
>>  GerV   ->     { being | leaving | going | ... }
>>
>>  AP     ->     (Adv*)+ (N) + A*
>>  A      ->     { old | biblical | bizarre | other | ... }
>>
>>
>>  VP     ->     V
>>         |      V     +   NP*
>>         |      V     +   NP*   +   PP*
>>         |      V     +   PP*
>>         |      V     +   S
>>         |      V     +   VP
>>         |      VP    +   AdvP
>>
>>  V      ->     { cry | code | give | appear | ... }
>>  V_c:s  ->     { think | believe | say | mean | ... }
>>  V_c:np ->     { want | find | leave | give | prefer | ... }
>>  V_c:vp ->     { want | try | need | prefer |... }
>>  V_c:pp ->     { fly | travel | ... }
>>
>>  AdvP   ->     Adv*
>>  Adv    ->     { now | far | here | even | badly | ... }
>>
>>
>>  PP     ->     Pre   +   NP
>>  Pre    ->     { at | in | on | by | for | since | ... }
>>
>>```
>
> _**(TG) Transformational Grammar**_
>> A generative grammar consisting of a CFG as a base, and derived trees through transformations.
>>
>> * **English Transformations:**
>>```
>>
>>  Imperative:   S     => VP
>>
>>  Yes-No Q:     S     => AUX   + NP  + VP
>>
>>  Subj Wh-:     S     => Wh-NP + VP
>>
>>  Obj Wh-:      S     => Wh-NP + AUX + S
>>
>>  Coordination: X     -> X     + CC  + C
>>                CC    -> { and | or | but | ... }
>>
>>```
>>
