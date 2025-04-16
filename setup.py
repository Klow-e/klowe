

# setup.py


from setuptools import setup, find_packages

setup(
    name = "KlowE",
    version = "1.0.0",
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
#        "logging",
#        "shutil",
    ],
)


# Clean Code Principles
# # The code should explain itself
# # The code should be type annotated
# # The code should be beautiful and regular
# # The code should be simple and easy
# # The code should be explicit and flat
# # The code should be defensive and errors be managed
# # The coude should ask forgiveness, not permission
# # A function should only do one thing only
# # One thing is when no other meaningful function can be extracted
# # If the implementation is hard to explain, it's a bad idea


# ToDo:
# # capitalize textprocessor functions
# # comment with ''' ''' function descriptions
# # add chi^2 to theory
# # create hebrew & greek parser

