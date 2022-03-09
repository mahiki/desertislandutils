# desertislandutils
Setup a python utilities repo.

## INCEP-DATE
```bash
cd $HOME/repo/python-dev

poetry new desertislandutils
cd desertislandutils

# with some movement to make util packages independent
../desertislandutils
    ├── notes
    │   ├── poetry-packaging-notes.md
    │   └── toobigdatadoc-dev-log.md
    ├── src
    │   └── toobigdatadoc
    │       ├── __init__.py
    │       └── __main__.py
    ├── tests
    │   ├── __init__.py
    │   └── test_desertislandutils.py
    ├── README.rst
    ├── poetry.lock
    └── pyproject.toml
```

## OFF-WORLD: STRUCTURE
Following this poetry project [hyper-inspector example poetry package][1] for python package conventions.

Will have to iterate once its clear what the package executable is exported as.

### github repo
after script skeleton is in



## BLUSH-RESPONSE: SCRIPT SKELETON
```bash
poetry shell
# Spawning shell within /Users/segovia/Library/Caches/pypoetry/virtualenvs/desertislandutils-AVSNhiuH-py3.9
# . /Users/segovia/Library/Caches/pypoetry/virtualenvs/desertislandutils-AVSNhiuH-py3.9/bin/activate

# add poetry dependency, not pathlib is in standard library
poetry add argparse

# (desertislandutils-AVSNhiuH-py3.9) Kehena segovia: ~/repo/python-dev/desertislandutils
poetry run python src/toobigdatadoc/too.py data
# arg1: data
# name: __main__
# TOO: you have successfully called the command line. Goodbye.

poetry run python src/toobigdatadoc/too.py --help
# usage: too [-h] {big,data,doc}

# Create symlinked parallel folders to contain data/binary files outside of git repo or away from source/text files.

# positional arguments:
#   {big,data,doc}  large files to exclude from backup, smallish datasets, binary files like pdf

# optional arguments:
#   -h, --help      show this help message and exit
```



----------
## CHEW
[1]: https://github.com/santiagobasulto/hyper-inspector

[python docs: packaging](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

[Important docs on poetry package TOML spec](https://python-poetry.org/docs/pyproject#packages)

[argparse: command line tool arg builder](https://docs.python.org/3/library/argparse.html)