

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


def PDFFileText(file_path: str) -> str:
    """
    Extracts the text from a PDF file.
    `param 1:  file path`
    `returns:  text`
    `example:  thetext: str = PDFFileText(mypdffile)`
    """
    with open(file_path, 'rb') as pdf:
        with open('pdf_bytes', 'wb') as fl:
            fl.write(pdf.read())
    lines: list[str] = extract_text('pdf_bytes').split("\n")
    lines: list[str] = [i.strip().replace('\x0c', '') for i in lines]
    lines: list[str] = ShortenList(lines)
    text: str = "\n".join(lines)
    os.remove('pdf_bytes')
    return text


def HTMLFileText(file_path: str) -> str:
    """
    Extracts the text from an HTML file.
    `param 1:  file path`
    `returns:  text`
    `example:  thetext: str = HTMLFileText(myhtmlfile)`
    """
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as html:  
        soup = BeautifulSoup(html.read(), 'html.parser')
    lines: list[str] = [p.text for p in soup.find_all('p')]
    lines: list[str] = [i.strip() for i in lines]
    lines: list[str] = ShortenList(lines)
    text: str = "\n".join(lines)
    return text


def FileToText(file_path: str) -> str:
    """
    Extracts the text from a file. Accepts HTML and PDF.
    `param 1:  file path`
    `returns:  text`
    `example:  thetext: str = FileToText(myhtmlfile)`
    """
    if file_path.endswith(".html"): return HTMLFileText(file_path)
    elif file_path.endswith(".pdf"): return PDFFileText(file_path)
    else: raise Exception(f"Invalid file type: {file_path}. Try PDF or HTML")


def FormXML(text: str, filename: str, uri: str = '') -> str:
    """
    Extracts the text from a file. Accepts HTML and PDF.
    `param 1:  text name`
    `param 1:  file name`
    `param 1:  URL string`
    `returns:  text formatted for xml corpus`
    `example:  xmltext: str = FormXML(mytext)`
    """
    xml_data: str = f"\n<text filename='{filename}' url='{uri}'>"
    for i in text.split('\n'): xml_data += f"\n<s>{i}</s>"
    xml_data += f"\n</text>\n"
    return xml_data


def WebPage(url: str) -> str:
    """
    Extracts the text from the contents in an URL, be it an HTML webpage or PDF.
    `param 1:  url string`
    `returns:  text in the contents of the page`
    `example:  webtext: str = WebPage('https://www.waysofenlichenment.net')`
    """
    response = requests.get(url, timeout=5)
    if response.status_code == 200:

        if url.endswith('.pdf'):
            with open('name', 'wb') as fl:
                fl.write(response.content)
            text: str = extract_text('name')
            os.remove('name')
            return text
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            paragraphs = [p.text for p in paragraphs]
            paragraphs = [i.strip().replace('\x0c', '') for i in paragraphs]
            paragraphs = " ".join(paragraphs)
            return paragraphs

    else: raise Exception(f"Unacceptable response '{response.status_code}' at '{url = }'")


def DownloadWebpage(filenamepath: str, url: str) -> None:
    """
    Extracts the text from the contents in an URL, be it an HTML webpage or PDF.
    `param 1:  relative path to output file, include file type with a prefix`
    `param 2:  url string`
    `returns:  None`
    `result:   webpage or online PDF downloaded at desired location`
    `example:  DownloadWebpage('mydownloads/lichen.html', 'https://www.waysofenlichenment.net')`
    """
    if filenamepath.endswith(('.pdf', '.html')) == False:
        print(f" Make sure to include a file type in the first argument, like 'file.pdf' or folder/file.html'.")

    response = requests.get(url, timeout=5)
    if response.status_code == 200:

        with open(f"{filenamepath}", 'wb') as fl:
            fl.write(response.content)

    else: raise Exception(f"Response error {response.status_code}")


###############################################################################################


def SearchLinks(url: str) -> list[str]:
    """
    Extracts hyperlinks from an URL.
    `param 1:  url string`
    `returns:  list of links in that page`
    `example:  linksinpage: list[str] = SearchLinks('https://www.waysofenlichenment.net')`
    """
    lang_code = {"en":"en,en", "es":"es-ES,es", "it":"it,it", "fr":"fr,fr"}.get("".join(KLanguage))
    headers = {'Accept-Language': lang_code, 'Accept' : '*/*', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3.1 Safari/605.1.15',}

    try:
        response = requests.get(url, headers = headers, timeout = 5)
        soup = BeautifulSoup(response.text, 'html.parser')
        links: list[str] = [str(i.get('href')) for i in soup.find_all('a')]
        links: list[str] = [i for i in links if i.startswith(('/', '#')) == False]
        links: list[str] = list(set(links))
        return links

    except Exception as e:
        print(f"Error: {e} in {url}")
        return [url, ]



def KWebScrap(project_name: str, query_terms: tuple[str, ...]) -> None:
    """
    1: Creates the directory structure for a web scraping project.
    2: Generates a list of combinations of temrs suitable for insertion in a searcher's URL.
    3: Searches online (with StartPage and Lycos) for the combinations, and extracts the results.
    4: Creates a txt and xml corpus based on the results and cleans it.
    5: Creates a zip file of the project.

    `param 1:  one str as the project's name`
    `param 2:  one tuple[str, ...] of at least three strings`
    `returns:  None`
    `result:   a directory is created with the scrapped corpus`
    `example:  KWebScrap("GNU", ("software libre", "sistema operativo", "distribución linux", "GNU"))`
    It's better if the terms are unequivocally in the desired language.
    Works fine on UNIX-based file systems, may fail on Windows.
    """

    if len(lang := "".join(KLanguage)) == 0: raise Exception(f"Language not set. Set it with KSetLanguage() as 'es', 'en', ...")
    if len(seeds := [f"%22{i}%22" for i in query_terms]) < 3: raise Exception(f"Must add at least 3 terms in a tuple as the second argument.")
    print(f"\nThe machine is thinking. This will take a couple of seconds.")

    CreateFolder(f"{project_name}")
    CreateFolder(f"{project_name}/downloads")
    CreateFolder(f"{project_name}/xml_corpus")
    CreateFolder(f"{project_name}/txt_corpus")
    CreateFile(f"{project_name}/generated_tuples.txt")

    search_tuples: list[str] = ["+".join(i).replace(" ", "+") for i in list(combinations(seeds, 3))]
    WriteOnFile(f"{project_name}/generated_tuples.txt", "\n".join(search_tuples))



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
        collected: list[str] = [j for k in [SearchLinks(i) for i in searches] for j in k]
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



    print(f"\nDownloading {len(clean_urls)} files... \nDon't mind errors. Takes about 1 minute per 100 files.\n")



    for i, j in enumerate(clean_urls):
        try:
            format = 'pdf' if j.endswith('.pdf') else 'html'
            DownloadWebpage(f"{project_name}/downloads/{project_name}_{i}.{format}", j)
            print(f"{format.upper(): <4} {i: <3} {j}")
        except Exception as e: print(f"Error '{e}' in URL {i: <3} {j}")
    print()



    logging.getLogger('pdfminer').setLevel(logging.ERROR)

    source = os.listdir(f"{project_name}/downloads")
    print(f"Creating {len(source)} xml and txt files from:")

    for i in source:

        texto: str = FileToText(f"{project_name}/downloads/{i}")
        uri: str = clean_urls[int(i.rstrip('.htmlpdf').removeprefix(f"{project_name}_"))]

        with open(f"{project_name}/xml_corpus/{i.rstrip('.htmlpdf')}.xml", 'w') as fl:
            fl.write(FormXML(texto, i, uri))

        with open(f"{project_name}/txt_corpus/{i.rstrip('.htmlpdf')}.txt", 'w') as fl:
            fl.write(texto)

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

