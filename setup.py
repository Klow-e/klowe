

# setup.py


# Copyright (C) 2025 Chloe Carral Bustillo <chloevampi01@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from setuptools import setup, find_packages

setup(
    name = "KlowE",
    version = "1.2.8",
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
#        "time",
#        "typing",
#        "dataclasses",
    ],
)

