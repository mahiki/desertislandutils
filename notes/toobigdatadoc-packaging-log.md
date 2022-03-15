## desertislandutils.toobigdatadoc package executable
OK poetry now is time to shine.

>I am developing python packages with poetry in isolated environment, and distributing executables to my home machine. These are utility programs I use all the time, currently bash.  *There is no need to import these modules into other packages.

1. CLI application for local terminal workflow
2. develop with poetry environment management
3. test build locally to create executable
    * python source code + dependencies and python interpreter in folder (like pipx)
    * single file executable, copied to ~/bin or homebrew (preferred if fast)
4. merge to main, initiate CI/CD build on github actions
5. homebrew to install || script to download to ~/bin

## INCEP-DATE: reconsidering shebang
* like bash scripts, python single file scripts run on a local interpreter
* but python applications are built within an isolated environment, therefore:
    * with many CLI tools, not all may fit with global environment (package versions, etc.)
* *I definitely want a test/build in CI/CD process, lets go all the way with python package development.

## INCEP-DATE
Not much on Poetry getting started page, but the [commands reference][pcli] has `build`. We want wheels only, which is the binary format.

```bash
# just give it a try
poetry build --format wheel
    # Building desertislandutils (0.1.0)
    #   - Building wheel
    #   - Built desertislandutils-0.1.0-py3-none-any.whl

# now there is a dist/ directory
l dist/
-rw-r--r-- 1 2.8K Mar 11 20:08 desertislandutils-0.1.0-py3-none-any.whl

```
### **Q: how to install executable from a whl binary?**
A: with pip

NOTE: pyproject needs following to get right module name:

    # poetry env ../bin/too
    from src.toobigdatadoc.__main__ import main
    # pyproject:
    [tool.poetry.scripts]
    too = 'src.toobigdatadoc.__main__:main'

```bash
# PASS: now that i fixed poetry script defn, this works now
poetry run too --help

# install within the Poetry environment
    #   (desertislandutils-AVSNhiuH-py3.9)
python3 -m pip install /Users/segovia/repo/python-dev/desertislandutils/dist/desertislandutils-0.1.0-py3-none-any.whl
which too
    # /Users/segovia/Library/Caches/pypoetry/virtualenvs/desertislandutils-AVSNhiuH-py3.9/bin/too

too --help
#   success, help file and working folder

cd ~/trashwork/poetrytest/desert2
too big
# PASS
```

FIXED: Absolutely no idea how to run my `too --help` command. The problem was in the ../bin/too script import namespace, noted above.

### pipx install wheel to global namespace
```bash
brew install pipx
pipx install /Users/segovia/repo/python-dev/desertislandutils/dist/desertislandutils-0.1.0-py3-none-any.whl

which too
    # /Users/segovia/repo/enviro-repo/osx-base/dotfiles/.local/bin/too

# did the import work right?
bat $(which too)
# File: /Users/segovia/repo/enviro-repo/osx-base/dotfiles/.local/bin/too
#    5   │ from src.toobigdatadoc.__main__ import main

too --help
~/trashwork/poetrytest/desert3
too data
# PASS: it works!


```
## OFF-WORLD: pipx
Actually, works great, can install to global space from wheels, directly from PyPi as well.

[pipx see below][px] has instructions for poetry users. it downloads from PyPi registry as envrionment-isolated executables.

Not sure from documentation if I'm getting binaries or not, lets test it out. **NOPE its just the source code along with dependent libraries**

* possible dev flow: `poetry (wheel) -> pypi -> pipx (<- executable name + script and libraries to ~/.local)`
* con: managing tools with pipx alongside brew
* pro: pipx is simple
* pro: many homebrew formula are essentially same deployment of python env + script file

```bash
brew install pipx
pipx ensurepath
source ~/.zshrc

pipx install pycowsay
    # creating shared libraries
    # etc
    # These apps are now globally available
        # - pycowsay

l bat /Users/segovia/repo/enviro-repo/osx-base/dotfiles/.local/pipx/venvs/pycowsay/lib/python3.10/site-packages/pycowsay/main.py
   1   │ #!/usr/bin/env python
   2   │ # -*- coding: utf-8 -*-
...
  10   │
  11   │ def main():
  12   │     if "--version" in sys.argv[1:]:
...
  27   │        \   ^__^
  28   │         \  (oo)\_______
  29   │            (__)\       )\/\\
  30   │                ||----w |
  31   │                ||     ||
...

# well i'm done with this.
pipx uninstall-all
brew uninstall pipx
trash $HOME/.local/bin $HOME/.local/pipx
```

## OFF-WORLD: pyinstall
[pyinstall][pyin] looks like the front runner, although must test to see.

hold on -- nuitka looking thicc right now.

## OFF-WORLD: **nuitka**
Stop the presses. Commercially supported product, Nuitka is a Python to C compiler where pyinstall is a zip file of all the python src and libs, the executable should be fast. And this:

>If you have a pyproject.toml driven creation of wheels for your software in place, putting Nuitka to use is extremely easy.

So this can integrate with my poetry workflow, I develop with poetry:

* poetry add, install, etc
* poetry build .. wheel..
* pyproject uses nuitka to build, posts executable to PyPi maybe
* homebrew formula maybe, or pipx install package? Or pip?
* global python pip env for all projects (poetry, nuitka/pyinstaller, ...)
  

```bash
# install nuitka into the 'global' python scope ie not in a poetry env
python3 -m pip install --upgrade nuitka

python3 -m nuitka --help

python3 -m nuitka --follow-imports --onefile program.py

# or use normal build process with pyproject and build backend defined
```



## EMPATHY
[pipx creates CLI executable, see cowsay example][px]
[pyinstaller suggested][pyin]
[pyinstaller github][pying]
[many suggested tools][sopy]
[packagingpython list of tools, including executable binary][packp]
[pyinstaller example][pyiex]
[so search 'python executable'][sopyex]


----------
[pcli]: https://python-poetry.org/docs/cli/
[pyin]: https://stackoverflow.com/questions/5458048/how-can-i-make-a-python-script-standalone-executable-to-run-without-any-dependen
[pying]: https://github.com/pyinstaller/pyinstaller
[sopy]: https://stackoverflow.com/questions/12059509/create-a-single-executable-from-a-python-project
[packp]: https://packaging.python.org/en/latest/overview/#packaging-python-applications
[pyiex]: https://github.com/Vikka/Meteor/releases
[sopiex]: https://stackoverflow.com/search?q=%5Bpython%5D+standalone+executable
[px]: https://pypi.org/project/pipx/
