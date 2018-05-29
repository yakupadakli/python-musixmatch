# Musixmatch

A library that provides a Python wrapper to [Musixmatch API](https://developer.musixmatch.com/).

## Installation

The easiest way to install the latest version
is by using pip/easy_install to pull it from PyPI:

    pip install python-musixmatch

You may also use Git to clone the repository from
Github and install it manually:

    git clone https://github.com/yakupadakli/python-musixmatch.git
    cd python-musixmatch
    python setup.py install

Python 2.7, 3.4, 3.5 and 3.6, is supported for now.


## Usage

    from musixmatch.api import Musixmatch
    
    api_key = ""
    musixmatch = Musixmatch(api_key)
