

# klowe/tokenization.py


###############################################################################################


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
esp_stopwords += ["que", "qué", "y", "e", "o", "pero", "porque", "por", "para", "ya", "como", "ni", "no", "sí", "con", "más", "mas", "tal"]
esp_stopwords += ["en", "entre", "cuando", "muy", "sin", "sobre", "también", "hasta", "donde", "desde", "durante", "contra", "ante", "antes", "hacia", "mediante", "tras", "según"]
esp_stopwords += ["el", "la", "los", "las", "a", "al", "de", "del", "lo", "le", "les", "un", "una", "uno", "unos", "quien", "otro", "otros", "otras", "otra", "alguno", "algunos", "alguna", "algunas"]
esp_stopwords += ["se", "si", "sus", "me", "mí", "yo", "él", "su", "nos", "ella", "ellos", "nosotros", "mi", "mis", "tú", "te", "ti", "tu", "tus", "ellas", "nosotras", "vosotros", "vosotras", "os", "mío", "mía", "míos", "mías", "tuyo", "tuya", "tuyos", "tuyas", "suyo", "suya", "suyos", "suyas", "nuestro", "nuestra", "nuestros", "nuestras", "vuestro", "vuestra", "vuestros", "vuestras"]
esp_stopwords += ["cada", "varios", "varias", "este", "esto", "esta", "estos", "estas", "esos", "ese", "eso" "esa", "esos", "esas", "aquello", "aquel", "aquella", "aquellos", "aquellas", "poca", "pocas", "pocos" "poco", "algo", "mucho", "muchos", "mucha", "muchas", "quienes", "nada", "muchos", "todos", "todo", "toda", "todas", "cual", "cualquier", "cuanquiera", "nada", "tanto", "tantos", "tanta", "tantas", "vez", "veces", "etc", "solo", "solamente", "mientras", "siguiente", "exclusivamente"]
esp_stopwords += ["soy", "eres", "es", "somos", "sois", "son", "sea", "seas", "seamos", "seáis", "sean", "seré", "serás", "será", "seremos", "seréis", "serán", "sería", "serías", "seríamos", "seríais", "serían", "era", "eras", "éramos", "erais", "eran", "fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron", "fuera", "fueras", "fuéramos", "fuerais", "fueran", "fuese", "fueses", "fuésemos", "fueseis", "fuesen"]
esp_stopwords += ["estar", "estás", "estoy", "estás", "está", "estamos", "estáis", "están", "esté", "estés", "estemos", "estéis", "estén", "estaré", "estarás", "estará", "estaremos", "estaréis", "estarán", "estaría", "estarías", "estaríamos", "estaríais", "estarían", "estaba", "estabas", "estábamos", "estabais", "estaban", "estuve", "estuviste", "estuvo", "estuvimos", "estuvisteis", "estuvieron", "estuviera", "estuvieras", "estuviéramos", "estuvierais", "estuvieran", "estuviese", "estuvieses", "estuviésemos", "estuvieseis", "estuviesen", "estando", "estado", "estada", "estados", "estadas", "estad"]
esp_stopwords += ["hay", "he", "has", "ha", "hemos", "habéis", "han", "haya", "hayas", "hayamos", "hayáis", "hayan", "habré", "habrás", "habrá", "habremos", "habréis", "habrán", "habría", "habrías", "habríamos", "habríais", "habrían", "había", "habías", "habíamos", "habíais", "habían", "hube", "hubiste", "hubo", "hubimos", "hubisteis", "hubieron", "hubiera", "hubieras", "hubiéramos", "hubierais", "hubieran", "hubiese", "hubieses", "hubiésemos", "hubieseis", "hubiesen", "habiendo", "habido", "habida", "habidos", "habidas"]
esp_stopwords += ["tengo", "tienes", "tiene", "tenemos", "tenéis", "tienen", "tenga", "tengas", "tengamos", "tengáis", "tengan", "tendré", "tendrás", "tendrá", "tendremos", "tendréis", "tendrán", "tendría", "tendrías", "tendríamos", "tendríais", "tendrían", "tenía", "tenías", "teníamos", "teníais", "tenían", "tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron", "tuviera", "tuvieras", "tuviéramos", "tuvierais", "tuvieran", "tuviese", "tuvieses", "tuviésemos", "tuvieseis", "tuviesen", "teniendo", "tenido", "tenida", "tenidos", "tenidas", "tened"]
esp_stopwords += ["sintiendo", "sentido", "sentida", "sentidas", "siente", "partir", "particular", "usualmente", "hizo"]
esp_stopwords += ["xix", "xxi", "xviii", "xvii", "xvi", "xiv", "xii", "vii", "iii", "vii", "cch", "skip", "isbn", "ocasiones"]

ita_stopwords: list[str] = []
ita_stopwords += ["ma", "ed", "se", "perché", "anche", "ad", "al", "allo", "ai", "agli", "all", "agl", "alla", "alle", "con", "col", "coi", "da", "dal", "dallo", "dai", "dagli", "dall", "dagl", "dalla", "dalle", "di", "del", "dello", "dei", "degli", "dell", "degl", "della", "delle", "in", "nel", "nello", "nei", "negli", "nell", "negl", "nella", "nelle", "su", "sul", "per", "tra", "contro"]
ita_stopwords += ["sullo", "sui", "sugli", "sull", "sugl", "sulla", "sulle", "io", "tu", "lui", "lei", "noi", "voi", "loro", "mio", "mia", "miei", "mie", "tuo", "tua", "tuoi", "tue", "suo", "sua", "suoi", "sue", "nostro", "nostra", "nostri", "nostre", "vostro", "vostra", "vostri", "vostre", "mi", "ti", "ci", "vi", "lo", "la", "li", "le", "gli", "ne", "il", "l"]
ita_stopwords += ["un", "uno", "una", "come", "dov", "dove", "che", "chi", "cui", "non", "più", "quale", "quanto", "quanti", "quanta", "quante", "quello", "quelli", "quella", "quelle", "questo", "questi", "questa", "queste", "si", "tutto", "tutti", "a", "c", "e", "i", "o"]
ita_stopwords += ["ho", "hai", "ha", "abbiamo", "avete", "hanno", "abbia", "abbiate", "abbiano", "avrò", "avrai", "avrà", "avremo", "avrete", "avranno", "avrei", "avresti", "avrebbe", "avremmo", "avreste", "avrebbero", "avevo", "avevi", "aveva", "avevamo", "avevate", "avevano", "ebbi", "avesti", "ebbe", "avemmo", "aveste", "ebbero", "avessi", "avesse", "avessimo", "avessero", "avendo", "avuto", "avuta", "avuti", "avute"]
ita_stopwords += ["sono", "sei", "è", "siamo", "siete", "sia", "siate", "siano", "sarò", "sarai", "sarà", "saremo", "sarete", "saranno", "sarei", "saresti", "sarebbe", "saremmo", "sareste", "sarebbero", "ero", "eri", "era", "eravamo", "eravate", "erano", "fui", "fosti", "fu", "fummo", "foste", "furono", "fossi", "fosse", "fossimo", "fossero", "essendo"]
ita_stopwords += ["faccio", "fai", "facciamo", "fanno", "faccia", "facciate", "facciano", "farò", "farai", "farà", "faremo", "farete", "faranno", "farei", "faresti", "farebbe", "faremmo", "fareste", "farebbero", "facevo", "facevi", "faceva", "facevamo", "facevate", "facevano", "feci", "facesti", "fece", "facemmo", "faceste", "fecero", "facessi", "facesse", "facessimo", "facessero", "facendo"]
ita_stopwords += ["sto", "stai", "sta", "stiamo", "stanno", "stia", "stiate", "stiano", "starò", "starai", "starà", "staremo", "starete", "staranno", "starei", "staresti", "starebbe", "staremmo", "stareste", "starebbero", "stavo", "stavi", "stava", "stavamo", "stavate", "stavano", "stetti", "stesti", "stette", "stemmo", "steste", "stettero", "stessi", "stesse", "stessimo", "stessero", "stando"]

stop_words: list[str] = []
stop_words.extend(esp_stopwords)
stop_words.extend(ita_stopwords)


###############################################################################################


def clean_text(text: str) -> str:
    text = text.lower()
    text = text.replace("'", " ")
    text = text.replace("  ", " ")
    text = text.replace("\n\n", "")
    text = text.replace("\u200b", "")
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


###############################################################################################

