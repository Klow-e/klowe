

# klowe/__init__.py


from .textprocessor import *
from .chisquare import *
from .webscraper import *
from .vectorspacemodel import *
from .mathstuff import *
from .datavisualization import *
from .pythontools import *


import json
import importlib.resources as pkg_resources


with pkg_resources.open_text(__name__, "gloss_example.json") as fp:
    gloss_ex = json.load(fp)


# ToDo:
# setlang exclude chars

