# package too big|data|doc in python
* refactor too script into python
* deploy package with poetry
* install via homebrew
* coreutils is great example of a mega repo of many utils

## PROJECT NAME: desertislandutils.too


## DOES POETRY SUPPORT MONOREPO BUILD?
[example monorepo in python with poetry](https://github.com/dermidgen/python-monorepo/)
[monorepo issue](https://github.com/python-poetry/poetry/issues/3368)
[monorepo issue 936](https://github.com/python-poetry/poetry/issues/936)
[monorepo issue 2270 with internal dependency chain](https://github.com/python-poetry/poetry/issues/2270)
[poetry workspace plugin to support monorepo](https://github.com/jacksmith15/poetry-workspace-plugin)
[poetry multiproject plugin](https://github.com/DavidVujic/poetry-multiproject-plugin#poetry-multiproject-plugin)

someone has a prototype, organize like this.

    ./
    |- .git/
    |- packages/
    |   |- foo/
    |   |   |- sources (foo.py or foo/__init__.py, with tests...)
    |   |   |- pyproject.toml
    |   |- bar/
    |   |   |- sources (...)
    |   |   |- pyproject.toml
    |- pyproject.toml

## RSRC
https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
https://stackoverflow.com/questions/22081209/find-the-root-of-the-git-repository-where-the-file-lives
https://stackoverflow.com/questions/54572785/create-symlink-with-pathlib
https://docs.python.org/3/library/pathlib.html


## PACKAGING
Q: local or homebrew?
A: i prefer CICD builds, github for example

### Python brew packages
https://asciinema.org
/opt/homebrew/Cellar/asciinema/2.1.0 (619 files, 8MB) *
https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/asciinema.rb
https://pypi.org/project/asciinema/

monorepo with many applications
https://www.gnu.org/software/coreutils
https://github.com/coreutils/coreutils
https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/coreutils.rb
/opt/homebrew/Cellar/coreutils/9.0_1/bin
    |--> /opt/homebrew/opt/coreutils/libexec/gnubin/

https://github.com/saulpw/homebrew-vd/blob/HEAD/Formula/visidata.rb
https://visidata.org/

https://httpie.io/
/opt/homebrew/Cellar/httpie/3.0.2 (1,135 files, 14.0MB) *
https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/httpie.rb
