

# setup.py


from setuptools import setup, find_packages

setup(
    name = "KlowE",
    version = "0.0.12",
    description = "Python package for NLP",
    author = "Chloe Carral Bustillo",
    author_email = "chloevampi01@gmail.com",
    url = "https://github.com/Klow-e/",
    license = "GNU General Public License",
    
    packages = find_packages(),
    install_requires=[
        "setuptools",
        "unidecode",
        "nltk",
        "numpy",
        "scipy",
        "wikipedia",
        "requests",
        "bs4",
        "dataclasses",
        "matplotlib",
#        "re",
#        "string",
#        "operator",
#        "math",
#        "os",
#        "json",
    ],
)

