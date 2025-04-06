

# setup.py


from setuptools import setup, find_packages

setup(
    name = "KlowE",
    version = "0.2.1",
    description = "Python package for NLP",
    author = "Chloe Carral Bustillo",
    author_email = "chloevampi01@gmail.com",
    url = "https://github.com/Klow-e/",
    license = "GNU General Public License",

    packages = find_packages(),
    install_requires=[
        "setuptools",
        "unidecode",
        "numpy",
        "requests",
        "bs4",
        "matplotlib",
        "pdfminer.six",
#        "collections",
#        "re",
#        "string",
#        "operator",
#        "math",
#        "os",
#        "json",
#        "datetime",
    ],
)

