

# klowe/pythontools.py


###############################################################################################


import os
import shutil
import math
import operator
from collections import Counter


###############################################################################################


def SortDict(dicc: dict|zip|list[tuple[str, int]]) -> dict:
    """
    Sorts a dict or zip from high to low based on its values.
    `param 1:  dict to be sorted`
    `returns:  the sorted dict`
    `example:  sdicc: dict = SortDict(dicc)`
    """
    sorted_d: dict = dict(sorted(dict(dicc).items(), key=operator.itemgetter(1), reverse=True))
    return sorted_d


def GetKeys(dicc: dict|list[dict]) -> list:
    """
    From a dict or list[dict], extracts all the keys.
    `param 1:  dict or list[dict]`
    `returns:  list of the keys of the dictionary/ies`
    `example:  mykeys: list = GetKeys(dicc)`
    If it's a list[dict], the output will be a list[list[<keys>]].
    """
    if type(dicc) == dict:
        return list(dicc.keys())
    elif type(dicc) == list:
        return [GetKeys(i) for i in dicc]


def GetValues(dicc: dict|list[dict]) -> list:
    """
    From a dict or list[dict], extracts all the values.
    `param 1:  dict or list[dict]`
    `returns:  list of the values of the dictionary/ies`
    `example:  myvalues: list = GetValues(dicc)`
    If it's a list[dict], the output will be a list[list[<values>]].
    """
    if type(dicc) == dict:
        return list(dicc.values())
    elif type(dicc) == list:
        return [GetValues(i) for i in dicc]


def ShortenList(lista: list[str]) -> list[str]:
    """
    Reduces series of empty string items in lists to just one.
    `param 1:  list[str]`
    `returns:  the list with series of '' reduced to one appearance`
    `example:  cleaner_l: list[str] = ShortenList(['one', '', '', '', 'two'])`
    """
    outlist: list[str] = []
    i: int = 0
    emptycount: int = 0

    while i < len(lista):
        item: str = lista[i]

        if item != '':
            outlist.append(item)
            emptycount: int = 0
        else:
            emptycount += 1
        i += 1

        outlist.append('') if emptycount == 1 else None
    return outlist


###############################################################################################


def CountDistribution(lista: list[str]) -> list[tuple[str, int]]:
    """
    Counts how many times each item of a list appears in it.
    `param 1:  list[str]`
    `returns:  list[tuple[str, int]] where tuples are each unique item and how many times it appears`
    `example:  words_distribution: list[tuple[str, int]] = CountDistribution(tokenized_text)`
    """
    counter: Counter = Counter(lista)
    return counter.most_common()


def NGrams(tok: list, n: int) -> list[tuple]:
    """
    Of a list of items and a desired length, returns n-grams.
    `param 1:  list of items`
    `param 2:  length of n-grams`
    `returns:  list[tuple] where tuples are each item followed by the next n items`
    `example:  mybigrams: list[tuple] = NGrams([1, 2, 3, 4, 5], 2)`
    """
    ngrams: list[tuple] = [tuple(tok[i: i + n]) for i in range(len(tok) - n + 1)]
    return ngrams


###############################################################################################


def RemoveFolder(name: str) -> None:
    """
    Removes a folder alongside its contents and any .zip file with the same name.
    `param 1:  relative path to folder`
    `returns:  None`
    `result:   folder deleted`
    `example:  RemoveFolder('myfolder')`
    """
    if os.path.exists(name):
        shutil.rmtree(name)
    if os.path.exists(f"{name}.zip"):
        os.remove(f"{name}.zip")


def RemoveFile(name: str) -> None:
    """
    Checks the existance of a file and removes it if so.
    `param 1:  relative path to file`
    `returns:  None`
    `result:   file deleted`
    `example:  RemoveFile('myfile')`
    """
    os.remove(name) if os.path.exists(name) else None


def CreateFolder(name: str) -> str:
    """
    Creates a folder if it doesn't already exist.
    `param 1:  relative path to folder`
    `returns:  relative path to file`
    `result:   folder created`
    `example:  CreateFolder('myfolder')`
    """
    os.makedirs(name) if not os.path.exists(name) else None
    return name


def CreateFile(name: str) -> str:
    """
    Creates a file if it doesn't already exist.
    `param 1:  relative path to file`
    `returns:  relative path to file`
    `result:   file created`
    `example:  CreateFile('myfolder/myfile.txt')`
    """
    if os.path.exists(name):
        pass
    else:
        with open(name, 'w') as fl: fl.write('')
    return name


def WriteOnFile(name: str, content: str) -> None:
    """
    Appends content on a file.
    `param 1:  relative path to file`
    `param 2:  content to append to it`
    `returns:  None`
    `result:   content writen on file`
    `example:  WriteOnFile('myfile.txt', '\nUwU')`
    """
    with open(name, 'a') as fl: fl.write(content)


###############################################################################################

