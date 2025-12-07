

# klowe/webscraper.py


###############################################################################################


from .textprocessor import *
from .pythontools import *

from unidecode import unidecode
from pdfminer.high_level import extract_text
from bs4 import BeautifulSoup
import requests
import os
import operator
from operator import *
import itertools
from itertools import *
import logging
import shutil
import time


###############################################################################################


def WebPage(url: str) -> str:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        paragraphs = [p.text for p in paragraphs]
        paragraphs = " ".join(paragraphs)
        return paragraphs
    elif response.status_code == 429:
        print(f"Error '429 Too Many Requests' at '{url = }'")
        print(f" The function will return str('no') for pipelining purposes and wait for 9 seconds to not stress the API.")
        time.sleep(9)
        return "no"
    else:
        print(f"Unacceptable response '{response.status_code}' at '{url = }'")
        print(f" The function will return str('no') for pipelining purposes")
        return "no"


def PDFtext(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        with open('name', 'wb') as fl:
            fl.write(response.content)
        text = extract_text('name')
        os.remove('name')
        return text
    else: raise Exception(f"Not found {url = }")


###############################################################################################


def search_engine(url: str) -> list[str]:
    lang_code = {"en":"en,en", "es":"es-ES,es", "it":"it,it", "fr":"fr,fr"}.get("".join(KLanguage))
    headers = {'Accept-Language': lang_code, 'Accept' : '*/*', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3.1 Safari/605.1.15',}
    try:
        response = requests.get(url, headers = headers, timeout = 5)
        soup = BeautifulSoup(response.text, 'html.parser')
        links: list[str] = [str(i.get('href')) for i in soup.find_all('a')]
        return links
    except Exception as e:
        print(f"Error: {e} in {url}")
        return [url, ]


def file_to_text(file_path: str) -> list[str]:

    def html_text(file_path: str) -> list[str]:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as html:  
            soup = BeautifulSoup(html.read(), 'html.parser')
        text = soup.find_all('p')
        text = "\n".join([p.text for p in text])
        text = [j for j in [i.strip() for i in text.split("\n")] if j != ""]
        return text

    def pdf_text(file_path: str) -> list[str]:
        with open(file_path, 'rb') as pdf:  
            with open('pdf_bytes', 'wb') as fl:
                fl.write(pdf.read())
        text = extract_text('pdf_bytes').split("\n")
        text = "\n".join([i.strip() for i in text])
        text = [j for j in [i.strip() for i in text.split("\n")] if j != ""]
        os.remove('pdf_bytes')
        return text
    
    if file_path.endswith(".html"): return html_text(file_path)
    elif file_path.endswith(".pdf"): return pdf_text(file_path)
    else: raise Exception(f"Invalid file type: {file_path}. Try PDF or HTML")


def KWebScrap(project_name: str, query_terms: tuple[str, ...]) -> None:

    """
    1: Creates the directory structure for a web scraping project.
    2: Generates a list of combinations of temrs suitable for insertion in a searcher's URL.
    3: Searches online (with StartPage and Lycos) for the combinations, and extracts the results.
    4: Creates a txt and xml corpus based on the results and cleans it.
    5: Creates a zip file of the project.
    `param 1:  one str as the project's name`
    `param 2:  one tuple[str, ...] of at least three string`
    `returns:  None`
    `result:   a directory is created with the scrapped corpus`
    `example:  KWebScrap("GNU", ("software libre", "sistema operativo", "distribución linux", "GNU"))`
    It's better if the terms are unequivocally in the desired language. EG.: 'FOSS' is okay for English,
    but use 'software libre' and 'código abierto' for Spanish.
    Works fine on UNIX-based file systems, may fail on Windows.
    """

    if len(lang := "".join(KLanguage)) == 0: raise Exception(f"Language not set. Set it with KSetLanguage() as 'es', 'en'...")
    if len(seeds := [f"%22{i}%22" for i in query_terms]) < 3: raise Exception(f"Must add at least 3 seeds to input_seeds()")
    search_tuples: list[str] = ["+".join(i).replace(" ", "+") for i in list(combinations(seeds, 3))]

    print(f"\nThe machine is thinking. This will take a couple of seconds.")
    os.makedirs(f"{project_name}") if not os.path.exists(f"{project_name}") else None
    os.makedirs(f"{project_name}/downloads") if not os.path.exists(f"{project_name}/downloads") else None
    os.makedirs(f"{project_name}/xml_corpus") if not os.path.exists(f"{project_name}/xml_corpus") else None
    os.makedirs(f"{project_name}/txt_corpus") if not os.path.exists(f"{project_name}/txt_corpus") else None
    with open(f"{project_name}/generated_tuples.txt", "w") as fl: fl.write("\n".join(search_tuples))

    def search_queries(url_query: str) -> list[str]:
        searchers: list[str] = [f"https://www.startpage.com/rvd/search?query={url_query}&language={lang}",
                                f"https://www.startpage.com/rvd/search?query={url_query}&language={lang}&page=2",
                                f"https://www.startpage.com/rvd/search?query={url_query}&language={lang}&page=3",
                                f"https://www.startpage.com/rvd/search?query={url_query}&language={lang}&page=4",
                                f"https://search4.lycos.com/web/?q={url_query}&language={lang}",
                                ]
        return searchers
    searches: list[str] = [j for k in [search_queries(i) for i in search_tuples] for j in k]

    if not os.path.exists(f"{project_name}/collected_links.txt"):
        with open(f"{project_name}/collected_links.txt", "w") as fl: fl.write("\n".join(searches))
        with open(f"{project_name}/collected_links.txt", "a") as fl: fl.write("\n")
        collected: list[str] = [j for k in [search_engine(i) for i in searches] for j in k]
        with open(f"{project_name}/collected_links.txt", "a") as fl:
            for i in collected: fl.write(f"{i}\n")
    else: None

    with open(f"{project_name}/collected_links.txt", 'r', encoding='utf8') as f:
        clean_urls: list[str] = list(set([i.removesuffix("\n") for i in f if i.startswith("htt")]))
    for i, l in enumerate(clean_urls):
        if l.startswith("https://search.lycos.com/"): clean_urls[i] = "https://" + l.partition("http%3A%2F%2F")[-1]
    clean_urls: list[str] = [i.replace(" ", "%20") for i in clean_urls if not i.endswith("...")]
    clean_urls: list[str] = [i.replace("%2F", "/") for i in clean_urls if len(i) != 8]
    exclude_domains: tuple = ("https://www.startpage", "https://us1-browse", "https://www.youtube", "https://blocksurvey",
                                "https://support.", "https://m.youtube", "https://play.", "http://www.tripod.", "https://www.google",
                                "https://twitter", "https://hackerone", "https://buttondown", "https://www.tiktok", "http://www.mail.",
                                "https://www.instagram", "https://app.startpage", "https://books.google", "https://www.facebook",
                                "https://translate.", "http://domains.", "https://advertising.", "http://weather.", "https://info.",
                                "https://gutl.jovenclub.", "https://www.hostinger.", "https://tabasco.gob.", "https://openexpoeurope",
                                "https://www.planbnoticias", "https://www.ibiblio", "https://linux.ciberaula", "https://www.fsf.org",
                                "https://search2", "https://antares.sip.", "https://www.reddit", "https://www.pccomponentes",
                                "http://angelfire", "https://mastodon", "https://x.com", "https://www.jovenclub", "https://www.lycos.com",
                                "https://search3", "https://search1", "https://docencia.tic.unam", "https://search4", "https://search.",
                                "https://eu1-browse", "https://eu2-browse", "https://www2.feandalucia", "https://www.ecured.cu",
                                "https://registration.", "https://www.lavozdigital.", "https://www.centraldereservas.", "https://www.abc.",
                                "https://www.trainvelling.com", "https://www.getyourguide", "https://www.renfe", "https://www.tripadvisor.",)
    clean_urls: list[str] = list(set([i for i in clean_urls if not i.startswith(exclude_domains)]))
    with open(f"{project_name}/cleaned_links.txt", "w") as fl: fl.write("\n".join(clean_urls))

    def download_webpage(project_name: str, filename: str, url: str):
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            with open(f"{project_name}/downloads/{filename}", 'wb') as fl:
                fl.write(response.content)
        else: raise Exception(f"Response error {response.status_code}")

    print(f"\nDownloading {len(clean_urls)} files... \nDon't mind errors. Takes about 1 minute per 100 files.\n")
    for i, j in enumerate(clean_urls):
        try:
            format = "pdf" if j.endswith(".pdf") else "html"
            download_webpage(f"{project_name}", f"{project_name}_{i}.{format}", j)
            print(f"{format.upper(): <4} {i: <3} {j}")
        except Exception as e: print(f"Error '{e}' in URL {i: <3} {j}")
    print()

    def create_xml(x: list, filename: str, uri: str):
        xml_data = f"\n<text filename='{filename}' url='{uri}'>"
        for i in x: xml_data += f"\n<s>{i}</s>"
        xml_data += f"\n</text>\n"
        return xml_data

    logging.getLogger('pdfminer').setLevel(logging.ERROR)
    source = os.listdir(f"{project_name}/downloads")
    print(f"Creating {len(source)} xml and txt files from:")
    for i in source:
        text_as_list = file_to_text(f"{project_name}/downloads/{i}")
        uri = clean_urls[int(i.rstrip('.htmlpdf').removeprefix(f"{project_name}_"))]
        with open(f"{project_name}/xml_corpus/{i.rstrip('.htmlpdf')}.xml", 'w') as fl:
            fl.write(create_xml(text_as_list, i, uri))
        with open(f"{project_name}/txt_corpus/{i.rstrip('.htmlpdf')}.txt", 'w') as fl:
            fl.write("\n".join(text_as_list))
        print(f" {i}")
    print()
    logging.getLogger('pdfminer').setLevel(logging.NOTSET)

    print(f"Removing useless files...")
    text_list = []
    for i in os.listdir(f"{project_name}/txt_corpus"):
        with open(f"{project_name}/txt_corpus/{i}", 'r') as fl:
            t = fl.read()
            t = clean_text(t)
            t = t.replace("\n", " ")
            t = (i, t)
        text_list.append(t)
    exclude_text: list[str] = [i for i,v in text_list if len(v) < 60]
    sw_ratio = [( i , (sum(t.split().count(w) for w in stop_words) / len(t.split())) ) for i, t in text_list if i not in exclude_text]
    exclude_text.extend([i for i,v in sw_ratio if v < 0.1])
    for i in exclude_text:
        print(f" Removed {i.replace('.txt', '')} from corpus")
        txt_path = os.path.join(f"{project_name}/txt_corpus", i)
        xml_path = os.path.join(f"{project_name}/xml_corpus", i.replace(".txt", ".xml"))
        os.remove(txt_path)
        os.remove(xml_path)
    print()

    shutil.make_archive(project_name, "zip", project_name)
    return None


###############################################################################################

