# desertislandutils.toobigdatadoc
* Setup a python utilities repo.
* is git repo?
    * YES: place at `tooroot` top level
    * NO: parallel directory path to file form `tooroot`

## TODO
TODO: unit test package

## IOYCSWISWYE
* This is working 100% now
* I like this argparse package, very easy to use.
* TOPDIR_NAME now global, I don't like passing this to every function down the line.
* TESTS:
    * I have here a prototype of tests that could incorporate into module
    * but must create fresh test folder and git repo, with cleanup
    * yes, but make test package

- [desertislandutils.toobigdatadoc](#desertislandutilstoobigdatadoc)
    - [TODO](#todo)
    - [IOYCSWISWYE](#ioycswiswye)
    - [INCEP-DATE](#incep-date)
    - [OFF-WORLD: STRUCTURE](#off-world-structure)
        - [github repo](#github-repo)
    - [BLUSH-RESPONSE: SCRIPT SKELETON](#blush-response-script-skeleton)
    - [BLUSH-RESPONSE: PARSE ARGS](#blush-response-parse-args)
    - [BLUSH-RESPONSE: GIT ROOT FOLDER](#blush-response-git-root-folder)
    - [BLUSH-RESPONSE: relative symlink creation](#blush-response-relative-symlink-creation)
    - [BLUSH-RESPONSE: too topdir](#blush-response-too-topdir)
    - [VOIGHT-KAMPFF: PASS regular folder](#voight-kampff-pass-regular-folder)
    - [VOIGHT-KAMPFF: PASS git repo folders](#voight-kampff-pass-git-repo-folders)
    - [CHEW](#chew)

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

DONE: repo added to github. remindme has thing to push to new github.

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

Fixed pyproject.toml:
```toml
[tool.poetry.scripts]
-too = 'toobigdatadoc.__main__:main'
+too = 'src.toobigdatadoc.__main__:main'
```

Now this works:
```bash
poetry run too --help
    # usage: too [-h] {big,data,doc}
```

## BLUSH-RESPONSE: PARSE ARGS
```python
try:
    args = parser.parse_args(['big'])
 except:
    pass

print("arg1: {}".format(args.topdir))
    # arg1: big

```
## BLUSH-RESPONSE: GIT ROOT FOLDER
PASS: git topdir folders and symlink are being created properly.

[stackoverflow git root folder][sogit]
[stackoverflow is git repo][isgit]

For a repo directory, every repo is getting a folder system rooted at topdir ($HOME/too___).
There is the potential for namespace collision.
Relative links are going too require repos are staying in same relative relationship to topdir, can fix it on a new system by moving the repo root to the relative location matching the symlinks.
Absolute links make the repo directory not portable on new machine (must unlink/relink).

Here in bash:

```bash
# toodoc
mkdir $HOME/toodoc/iterm-colors
ln -s ../../../toodoc/iterm-colors doc

```py
import git

# is it a git repo?
def is_git_repo(path):
    try:
        _ = git.Repo(path, search_parent_directories=True)
        return True
    except git.exc.InvalidGitRepositoryError:
        return False

# find path of root
repo = git.Repo('.', search_parent_directories=True)
repo_root = repo.working_tree_dir

# relative path from repo root
repo_root = get_repo_root(Path.cwd())
    # PosixPath('/Users/segovia/repo/python-dev/desertislandutils')
curdir = Path.cwd()
    # PosixPath('/Users/segovia/repo/python-dev/desertislandutils/src/toobigdatadoc')
curdir.relative_to(repo_root)
    # PosixPath('src/toobigdatadoc')



# shell based git root
repo_dir = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')

# as a function
import subprocess
def getGitRoot():
    return subprocess.Popen(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')
```

## BLUSH-RESPONSE: relative symlink creation
* pathlib doesnt support creating relative symlink, although GNU ln -s does:
* could call the shell, invites other problems though
* i guess assemble all those dots manually by counting sections

```bash
ln -s --relative /Users/segovia/toobig/desertislandutils/tests/big_folder_test bigg
ls
    # bigg -> ../../../../../toobig/desertislandutils/tests/big_folder_test
```

```python
relative_to_home = Path.cwd().relative_to(Path.home())
    # PosixPath('repo/python-dev/desertislandutils/tests/big_folder_test')

# notice that the CWD relative to HOME has 5 elements:
os.listdir('../../../../../')
    # home folder contents

# CREATE RELATIVE PATH FROM STRING
pathstring = str(relative_to_home)
levels_to_home = len(pathstring.split('/'))           # breaking Windows compatibility
    # 5

dots_home = '../' * levels_to_home
Path(dots_home) / topname
```

## BLUSH-RESPONSE: too topdir
Here's what I'm going for in bash:
```bash
# Kehena segovia: ~/andromeda/school-search/spruce-street

mkdir -p $HOME/toodoc/andromeda/school-search/spruce-street
ln -s ../../../toodoc/andromeda/school-search/spruce-street doc
ls -l
lrwxr-xr-x 1  53 Mar  9 19:54 doc -> ../../../toodoc/andromeda/school-search/spruce-street
```

1. find relative path to $HOME
2. append full path from home
3. create directory
4. create simlink

```py
# get CWD
import os
print(os.getcwd())

# stdlib pathlib has current directory of file
import pathlib
current_dir = pathlib.Path('.').parent
current_file = pathlib.Path(__file__)

# symlinks
from pathlib import Path
Path('textfile.txt').write_text('hello world!')
Path('link-to-textfile.txt').symlink_to(Path('textfile.txt'))
```

## VOIGHT-KAMPFF: PASS regular folder
```bash
# PASS: regular folder location

# PASS: help flag
cd  ~/andromeda/finance/kapital/stelar
python $HOME/repo/python-dev/desertislandutils/src/toobigdatadoc/__main__.py --help
    # usage: too [-h] {big,data,doc}

    # Create symlinked parallel folders to contain data/binary files outside of git repo or away from source/text files.

    # positional arguments:
    #   {big,data,doc}  large files to exclude from backup, smallish datasets, binary files like pdf

    # optional arguments:
    #   -h, --help      show this help message and exit


# PASS: invalid arguments, > 1 args, 0 args
python $HOME/repo/python-dev/desertislandutils/src/toobigdatadoc/__main__.py 42
    # usage: too [-h] {big,data,doc}
    # too: error: argument arg1: invalid choice: '42' (choose from 'big', 'data', 'doc')

python $HOME/repo/python-dev/desertislandutils/src/toobigdatadoc/__main__.py pee poo
python $HOME/repo/python-dev/desertislandutils/src/toobigdatadoc/__main__.py doc poo
    # usage: too [-h] {big,data,doc}
    # too: error: unrecognized arguments: poo

# PASS: correct arg doc/big/data
    # initial failure, change TOPDIR_NAME to a global
# PASS: all doc/data/big
python $HOME/repo/python-dev/desertislandutils/src/toobigdatadoc/__main__.py doc

# PASS: symlink and files created for each
for file in */*.txt; do
bat $file
done

# PASS topdir contents
for dir in 'toobig' 'toodata' 'toodoc'; do
ls -1 ~/$dir/**/testfile.txt
done | sort
    # /Users/segovia/toobig/andromeda/finance/kapital/stelar/testfile.txt
    # /Users/segovia/toodata/andromeda/finance/kapital/stelar/testfile.txt
    # /Users/segovia/toodoc/andromeda/finance/kapital/stelar/testfile.txt
```

## VOIGHT-KAMPFF: PASS git repo folders
```bash
cd  ~/repo/datasci/biq/biq-206

# PASS: help flag, --help 42, 42 --help
python $HOME/repo/python-dev/desertislandutils/src/toobigdatadoc/__main__.py --help

# PASS: invalid arguments, > 1 args, 0 args
python $HOME/repo/python-dev/desertislandutils/src/toobigdatadoc/__main__.py 42
python $HOME/repo/python-dev/desertislandutils/src/toobigdatadoc/__main__.py pee poo
python $HOME/repo/python-dev/desertislandutils/src/toobigdatadoc/__main__.py doc poo

# PASS: valid args big/data/doc
python $HOME/repo/python-dev/desertislandutils/src/toobigdatadoc/__main__.py doc
python $HOME/repo/python-dev/desertislandutils/src/toobigdatadoc/__main__.py big
python $HOME/repo/python-dev/desertislandutils/src/toobigdatadoc/__main__.py data

for dir in 'big' 'data' 'doc'; do
    cat << EOF > $dir/testfile.txt
    This is a hypothetical large data file in a symlinked directory.
    Developing utility script 'too'
EOF
done

# check symlink correct
for file in */*.txt; do
bat $file
done

# check topdir contents
for dir in 'toobig' 'toodata' 'toodoc'; do
ls -1 ~/$dir/**/testfile.txt
done | sort
    # /Users/segovia/toobig/datasci/biq/biq-206/testfile.txt
    # /Users/segovia/toodata/datasci/biq/biq-206/testfile.txt
    # /Users/segovia/toodoc/datasci/biq/biq-206/testfile.txt

```



----------
## CHEW
[1]: https://github.com/santiagobasulto/hyper-inspector

[python docs: packaging](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

[Important docs on poetry package TOML spec](https://python-poetry.org/docs/pyproject#packages)

[argparse: command line tool arg builder](https://docs.python.org/3/library/argparse.html)

[sogit]: https://stackoverflow.com/questions/22081209/find-the-root-of-the-git-repository-where-the-file-lives

[isgit]: https://stackoverflow.com/questions/2044574/determine-if-directory-is-under-git-control
