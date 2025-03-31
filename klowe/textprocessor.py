

# klowe/textprocessor.py


###############################################################################################


from .webscraper import *
from .pythontools import *

import re
import string
from unidecode import unidecode


###############################################################################################


dirty_characters: str = string.punctuation
dirty_characters += string.digits
dirty_characters += "¿¡““»«…©"


esp_characters: str = "áéíóúüñç"
ita_characters: str = "àèìòùâêîôûãõäëïöüÿ"
legal_characters: str = string.ascii_letters
legal_characters += esp_characters
legal_characters += ita_characters


esp_stopwords: list[str] = []
esp_stopwords += ["que", "qué", "y", "e", "o", "pero", "porque", "por", "para", "ya", "como", "ni", "no", "sí", "con", "más", "mas", "tal", "cuyo", "así"]
esp_stopwords += ["en", "entre", "cuando", "muy", "sin", "sobre", "también", "tambien", "hasta", "donde", "desde", "durante", "contra", "ante", "antes", "hacia", "mediante", "tras", "según"]
esp_stopwords += ["el", "la", "los", "las", "a", "al", "de", "del", "lo", "le", "les", "un", "una", "uno", "unos", "dos", "quien", "otro", "otros", "otras", "otra", "alguno", "algunos", "alguna", "algunas"]
esp_stopwords += ["se", "si", "sus", "me", "mí", "yo", "él", "su", "nos", "ella", "ellos", "nosotros", "mi", "mis", "tú", "te", "ti", "tu", "tus", "ellas", "nosotras", "vosotros", "vosotras", "os", "mío", "mía", "míos", "mías", "tuyo", "tuya", "tuyos", "tuyas", "suyo", "suya", "suyos", "suyas", "nuestro", "nuestra", "nuestros", "nuestras", "vuestro", "vuestra", "vuestros", "vuestras"]
esp_stopwords += ["cada", "varios", "varias", "este", "esto", "esta", "estos", "estas", "esos", "ese", "eso" "esa", "esos", "esas", "aquello", "aquel", "aquella", "aquellos", "aquellas", "poca", "pocas", "pocos" "poco", "algo", "mucho", "muchos", "mucha", "muchas", "quienes", "nada", "muchos", "todos", "todo", "toda", "todas", "cual", "cualquier", "cuanquiera", "nada", "tanto", "tantos", "tanta", "tantas", "vez", "veces", "etc", "solo", "solamente", "mientras", "siguiente", "exclusivamente"]
esp_stopwords += ["soy", "eres", "es", "somos", "sois", "son", "sea", "seas", "seamos", "seáis", "sean", "seré", "serás", "será", "seremos", "seréis", "serán", "sería", "serías", "seríamos", "seríais", "serían", "era", "eras", "éramos", "erais", "eran", "fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron", "fuera", "fueras", "fuéramos", "fuerais", "fueran", "fuese", "fueses", "fuésemos", "fueseis", "fuesen"]
esp_stopwords += ["estar", "estás", "estoy", "estás", "está", "estamos", "estáis", "están", "esté", "estés", "estemos", "estéis", "estén", "estaré", "estarás", "estará", "estaremos", "estaréis", "estarán", "estaría", "estarías", "estaríamos", "estaríais", "estarían", "estaba", "estabas", "estábamos", "estabais", "estaban", "estuve", "estuviste", "estuvo", "estuvimos", "estuvisteis", "estuvieron", "estuviera", "estuvieras", "estuviéramos", "estuvierais", "estuvieran", "estuviese", "estuvieses", "estuviésemos", "estuvieseis", "estuviesen", "estando", "estado", "estada", "estados", "estadas", "estad"]
esp_stopwords += ["hay", "he", "has", "ha", "hemos", "habéis", "han", "haya", "hayas", "hayamos", "hayáis", "hayan", "habré", "habrás", "habrá", "habremos", "habréis", "habrán", "habría", "habrías", "habríamos", "habríais", "habrían", "había", "habías", "habíamos", "habíais", "habían", "hube", "hubiste", "hubo", "hubimos", "hubisteis", "hubieron", "hubiera", "hubieras", "hubiéramos", "hubierais", "hubieran", "hubiese", "hubieses", "hubiésemos", "hubieseis", "hubiesen", "habiendo", "habido", "habida", "habidos", "habidas"]
esp_stopwords += ["tengo", "tienes", "tiene", "tenemos", "tenéis", "tienen", "tenga", "tengas", "tengamos", "tengáis", "tengan", "tendré", "tendrás", "tendrá", "tendremos", "tendréis", "tendrán", "tendría", "tendrías", "tendríamos", "tendríais", "tendrían", "tenía", "tenías", "teníamos", "teníais", "tenían", "tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron", "tuviera", "tuvieras", "tuviéramos", "tuvierais", "tuvieran", "tuviese", "tuvieses", "tuviésemos", "tuvieseis", "tuviesen", "teniendo", "tenido", "tenida", "tenidos", "tenidas", "tened"]
esp_stopwords += ["sintiendo", "sentido", "sentida", "sentidas", "siente", "partir", "particular", "usualmente", "hizo", "usa", "pueden", "encontrar", "encuentran", "debe", "ocasiones", "sido", "ser"]

ita_stopwords: list[str] = []
ita_stopwords += ["ma", "ed", "se", "perché", "anche", "ad", "al", "allo", "ai", "agli", "all", "agl", "alla", "alle", "con", "col", "coi", "da", "dal", "dallo", "dai", "dagli", "dall", "dagl", "dalla", "dalle", "di", "del", "dello", "dei", "degli", "dell", "degl", "della", "delle", "in", "nel", "nello", "nei", "negli", "nell", "negl", "nella", "nelle", "su", "sul", "per", "tra", "contro"]
ita_stopwords += ["sullo", "sui", "sugli", "sull", "sugl", "sulla", "sulle", "io", "tu", "lui", "lei", "noi", "voi", "loro", "mio", "mia", "miei", "mie", "tuo", "tua", "tuoi", "tue", "suo", "sua", "suoi", "sue", "nostro", "nostra", "nostri", "nostre", "vostro", "vostra", "vostri", "vostre", "mi", "ti", "ci", "vi", "lo", "la", "li", "le", "gli", "ne", "il", "l"]
ita_stopwords += ["un", "uno", "una", "come", "dov", "dove", "che", "chi", "cui", "non", "più", "quale", "quanto", "quanti", "quanta", "quante", "quello", "quelli", "quella", "quelle", "questo", "questi", "questa", "queste", "si", "tutto", "tutti", "a", "c", "e", "i", "o"]
ita_stopwords += ["ho", "hai", "ha", "abbiamo", "avete", "hanno", "abbia", "abbiate", "abbiano", "avrò", "avrai", "avrà", "avremo", "avrete", "avranno", "avrei", "avresti", "avrebbe", "avremmo", "avreste", "avrebbero", "avevo", "avevi", "aveva", "avevamo", "avevate", "avevano", "ebbi", "avesti", "ebbe", "avemmo", "aveste", "ebbero", "avessi", "avesse", "avessimo", "avessero", "avendo", "avuto", "avuta", "avuti", "avute"]
ita_stopwords += ["sono", "sei", "è", "siamo", "siete", "sia", "siate", "siano", "sarò", "sarai", "sarà", "saremo", "sarete", "saranno", "sarei", "saresti", "sarebbe", "saremmo", "sareste", "sarebbero", "ero", "eri", "era", "eravamo", "eravate", "erano", "fui", "fosti", "fu", "fummo", "foste", "furono", "fossi", "fosse", "fossimo", "fossero", "essendo"]
ita_stopwords += ["faccio", "fai", "facciamo", "fanno", "faccia", "facciate", "facciano", "farò", "farai", "farà", "faremo", "farete", "faranno", "farei", "faresti", "farebbe", "faremmo", "fareste", "farebbero", "facevo", "facevi", "faceva", "facevamo", "facevate", "facevano", "feci", "facesti", "fece", "facemmo", "faceste", "fecero", "facessi", "facesse", "facessimo", "facessero", "facendo"]
ita_stopwords += ["sto", "stai", "sta", "stiamo", "stanno", "stia", "stiate", "stiano", "starò", "starai", "starà", "staremo", "starete", "staranno", "starei", "staresti", "starebbe", "staremmo", "stareste", "starebbero", "stavo", "stavi", "stava", "stavamo", "stavate", "stavano", "stetti", "stesti", "stette", "stemmo", "steste", "stettero", "stessi", "stesse", "stessimo", "stessero", "stando"]

eng_stopwords: list[str] = []
eng_stopwords += ["s", "t", "ll", "d", "ve", "re", "y", "m", "o", "a", "an", "the", "no", "nor", "not", "or", "so", "to"]
eng_stopwords += ["i", "my", "me", "myself", "she", "her", "hers", "herself", "he", "his", "him", "himself", "it", "its", "itself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves"]
eng_stopwords += ["be", "being", "do", "don", "does", "doesn", "doing", "did", "didn", "have", "has", "having", "hasn", "had", "hadn"]
eng_stopwords += ['about', 'above', 'after', 'again', 'against', 'ain', 'all', 'am', 'and', 'any', 'are', 'aren', 'as', 'at', 'because', 'been', 'before', 'below', 'between', 'both', 'but', 'by', 'can', 'couldn', "could"]
eng_stopwords += ["here", 'how', 'if', 'in', 'into', 'is', 'isn', 'just', 'mightn', "might", 'down', 'during', 'each', 'few', 'for', 'from', 'further']
eng_stopwords += ['more', 'most', 'mustn', "must", 'needn', "need", 'now', 'of', 'off', 'on', 'once', 'only', 'other', 'out', 'over', 'own', 'same']
eng_stopwords += ['should', 'shouldn', 'some', 'such', 'than', 'that', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those']
eng_stopwords += ['through', 'too', 'under', 'until', 'up', 'very', 'was', 'wasn', 'were', 'weren', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'won', 'wouldn']

fre_stopwords: list[str] = []
fre_stopwords += ['au', 'aux', 'avec', 'ce', 'ces', 'dans', 'de', 'des', 'du', 'elle', 'en', 'et', 'eux', 'il', 'ils', 'je', 'la', 'le', 'les', 'leur', 'lui', 'ma', 'mais', 'me', 'même', 'mes', 'moi', 'mon', 'ne', 'nos', 'notre', 'nous', 'on', 'ou', 'par', 'pas', 'pour', 'qu', 'que', 'qui', 'sa', 'se', 'ses', 'son', 'sur', 'ta', 'te', 'tes', 'toi', 'ton', 'tu', 'un', 'une', 'vos', 'votre', 'vous', 'c', 'd', 'j', 'l', 'à', 'm', 'n', 's', 't', 'y', 'été', 'étée', 'étées', 'étés', 'étant', 'étante', 'étants', 'étantes', 'suis', 'es', 'est', 'sommes', 'êtes', 'sont', 'serai', 'seras', 'sera', 'serons', 'serez', 'seront', 'serais', 'serait', 'serions', 'seriez', 'seraient', 'étais', 'était', 'étions', 'étiez', 'étaient', 'fus', 'fut', 'fûmes', 'fûtes', 'furent', 'sois', 'soit', 'soyons', 'soyez', 'soient', 'fusse', 'fusses', 'fût', 'fussions', 'fussiez', 'fussent', 'ayant', 'ayante', 'ayantes', 'ayants', 'eu', 'eue', 'eues', 'eus', 'ai', 'as', 'avons', 'avez', 'ont', 'aurai', 'auras', 'aura', 'aurons', 'aurez', 'auront', 'aurais', 'aurait', 'aurions', 'auriez', 'auraient', 'avais', 'avait', 'avions', 'aviez', 'avaient', 'eut', 'eûmes', 'eûtes', 'eurent', 'aie', 'aies', 'ait', 'ayons', 'ayez', 'aient', 'eusse', 'eusses', 'eût', 'eussions', 'eussiez', 'eussent']

universal_stopwords: list[str] = ["displaystyle", "chh", "skip", "isbn", "xix", "xxi", "xviii", "xvii", "xvi", "xiv", "xii", "vii", "iii", "vii", "aai"]

stop_words: list[str] = []

KLanguage: list = []
def set_language(lang: str):
    KLanguage.clear()
    KLanguage.extend(lang)
    stop_words.clear()
    stop_words.extend(universal_stopwords)
    match lang:
        case "es": stop_words.extend(esp_stopwords)
        case "it": stop_words.extend(ita_stopwords)
        case "en": stop_words.extend(eng_stopwords)
        case "fr": stop_words.extend(fre_stopwords)
        case _: stop_words.extend(esp_stopwords)
    print(KLanguage)
    return KLanguage


###############################################################################################


def clean_text(text: str) -> str:
    text = text.lower()
    text = text.replace("'", " ")
    text = text.replace("  ", " ")
    text = text.replace("\n\n", "")
    text = text.replace("\u200b", "")
    text = text.replace("—", ",")
    for i in dirty_characters: text = text.replace(i, "")
    return text


def tokenization(text: str) -> list[str]:
    clear_text: str = clean_text(text)
    tokens: list[str] = list(clear_text.split())
    for i in tokens:
        if all(j not in legal_characters for j in i):
            tokens.remove(i)
    tokens = [unidecode(k) for k in tokens]
    return tokens


def bagwords(text: str) -> list[str]:
    tokens: list[str] = tokenization(text)
    tokens = [i for i in tokens if len(i) > 2]
    tokens = [i for i in tokens if len(i) < 25]
    s_w = list(set([unidecode(s) for s in stop_words]))
    tokens = [j for j in tokens if j not in s_w]
    return tokens


def tdistribution(text: str) -> list[tuple[str, int]]:
    tokens: list[str] = tokenization(text)
    tokens: list[tiple[str, int]] = CountDistribution(tokens)
    return tokens


def btdistribution(text: str) -> list[tuple[str,int]]:
    tokens: list[str] = bagwords(text)
    tokens: list[tiple[str, int]] = CountDistribution(tokens)
    return tokens

###############################################################################################


def count_letters(text: str) -> int:
    clear_text: str = clean_text(text)
    n_letters: int = len(text.replace(" ", ""))
    return n_letters


def count_tokens(text: str) -> int:
    tokens: list[str] = tokenization(text)
    n_tokens: int = len(tokens)
    return n_tokens


def list_types(text: str) -> list[str]:
    tokens: list[str] = tokenization(text)
    types: set[str] = list(sorted(set(tokens)))
    return types


def count_types(text: str) -> int:
    n_types: int = len(list_types(text))
    return n_types


def typetoken_ratio(text: str) -> float:
    n_types: int = count_types(text)
    n_tokens: int = count_tokens(text)
    ttr: float = (n_types / n_tokens)
    return ttr


def average_toklen(text: str) -> int:
    lperw: float = count_letters(text) / count_tokens(text)
    return lperw


###############################################################################################


def sentence_tokenization(text: str) -> list[str]:

    def handle_wikipedia(text: str) -> str:
        text = text.replace("\u200b", "")
        wikih_pattern = r'== .+ =='
        if re.search(wikih_pattern, text):
            for m in re.findall(wikih_pattern, text):
                text = text.replace(m, m+". ")
        wikic_pattern = r'\S\.\[\d+\]\s'
        if re.search(wikic_pattern, text):
            for m in re.findall(wikic_pattern, text):
                text = text.replace(m, m[0]+" "+m[2:-1]+". ")
        return text

    def handle_numerals(p0: list[str]) -> list[str]:
        for i, v in enumerate(p0):
            if any(d in v for d in string.digits) and not v.endswith((".", "?", "!")):
                p0[i] += " " + p0.pop(i+1)
        return p0

    def handle_honor(p0: list[str]) -> list[str]:
        honor_pattern = r'[A-Z][a-z]{0,2}\.'
        def honor_case(p0: list[str]) -> list[str]:
            if re.search(honor_pattern, text):
                for i, v in enumerate(p0):
                    if re.match(honor_pattern, v):
                        if i + 1 < len(p0):
                            p0[i] += " " + p0.pop(i + 1)
                        else: break
            return p0
        for _ in range(len(re.findall(honor_pattern, text))):
            p0 = honor_case(p0)
        return p0

    def handle_comments(p0: list[str]) -> list[str]:
        comment_pattern = r'\((.*?)\)|\[(.*?)\]|\{(.*?)\}|\"(.*?)\"|\'(.*?)\'|\«(.*?)\»|\“(.*?)\”|¡(.*?)!|\¿(.*?)\?'
        comment_matches = max(len(i.split()) for m in re.findall(comment_pattern, text) for i in m if i) + 1
        comment_borders = [("(", ")"), ("[", "]"), ("{", "}"), (r'"', r'"'), (r"'", r"'"), ("«", "»"), ("“", "“"), ("¿", "?"), ("¡", "!")]
        def comment_case(p1: list[str], open_close: tuple[str, str]) -> list[str]:
            open_char, close_char = open_close
            i = 0
            while i < len(p1):
                if p1[i].startswith(open_char) and close_char not in p1[i]:
                    p1[i] += " " + p1.pop(i+1)
                else: i += 1
            return p1
        for _ in range(comment_matches):
            for b in comment_borders:
                p0 = comment_case(p0, b)
        return p0

    def handle_endings(p0: list[str]) -> list[str]:
        def ending_cases(p1: list[str]) -> list[str]:
            i = 0
            while i < len(p1) - 1:
                if not p1[i].endswith((".", "?", "!")):
                    p1[i] += " " + p1.pop(i + 1)
                else: i += 1
            return p1
        loops = text.count(". ") + text.count(".\n") + text.count("? ") + text.count("! ")
        for _ in range(loops):
            p0 = ending_cases(p0)
        return p0

    text = handle_wikipedia(text)
    p0 = text.split()
    p0 = handle_numerals(p0)
    p0 = handle_honor(p0)
    p0 = handle_comments(p0)
    p0 = handle_endings(p0)

    return p0


def count_sentences(text: str) -> int:
    sentences: list[str] = sentence_tokenization(text)
    n_sentences: int = len(sentences)
    return n_sentences


def wordspersentence(text: str) -> float:
    wpers: float = count_tokens(text) / count_sentences(text)
    return wpers


###############################################################################################

