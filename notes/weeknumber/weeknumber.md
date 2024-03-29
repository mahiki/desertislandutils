# WN: Week Number
I need to know the ISO reporting week for the current date all the time. And I like to be able to get the week number for any arbitrary date, usually this is in SQL but a CLI script also good.

This has been working fine in bash for years, but time to thaw out my python package development.
Also, its time to incorporate `justfile` into my package development workflow, so much easier to document commands that way.

Typer is pretty sweet, waaay beyond Argparse.

TODO: release is merged, need to GHA auto push to homebrew. See below, i think was manual change to tab formula.
The tap is referencing the mahiki/desertislandtils release page with tar.gz per version.
TODO: GHA create a release
TODO: brew tap create tag and push updated URLs commit.

## REQUIREMENTS
Options:
    input date, default current date
    Week ending day, default saturday (ISO minus 1)

Dependencies:
[Typer CLI package instead of ArgParse](https://typer.tiangolo.com/tutorial/first-steps/)
Pendulum date package
Just -- yes tis time

[Typer Build Poetry Package Example](https://typer.tiangolo.com/tutorial/package/#generate-docs-with-typer-cli-optional)
[Typer Cli install](https://typer.tiangolo.com/typer-cli/)

## CHEWS PLACE
```sh
poetry env use 3.11
poetry add "typer[all]" 
poetry add pendulum="~2.0"
# note pendulum 2.1.2 kept failing build, I went through this before
poetry install

# add script name to pyproject:
[tool.poetry.scripts]
wn = "src.weeknumber.wn:app"
```

At this point I can try the app:
```sh
poetry shell
(desertislandutils-py3.11) $> wn --help
```
actually its expecting a command, gotta figure single command app.

## TEARS IN RAIN
**It works great!**

```sh
wn --help

 Usage: wn [OPTIONS] [DATE]

 ISO year week number of a date as YYYY-WDD. Default weekend day is Sat.
 Example:
 $> wn 'Jul 22'
 2023-W29

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   date      [DATE]  A text expression of date, ex: 'November 27', or 2112-07-29 [default: (dynamic)]                                 │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --sunday                                  Weekend is Saturday by default, this flag sets Sunday weekend day.                         │
│ --last                                    Give week number of most recently completed week (overrides DATE argument).                │
│ --verbose               --no-verbose      [default: no-verbose]                                                                      │
│ --install-completion                      Install completion for the current shell.                                                  │
│ --show-completion                         Show completion for the current shell, to copy it or customize the installation.           │
│ --help                                    Show this message and exit.                                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

wn 2112-07-24 --sunday --verbose
# Input date string: 2112-07-24
# Timezone: US/Pacific
# Parsed date: 2112-07-24
# ISO week number:
# 2112-W29

wn 2112-07-24 --verbose
# Input date string: 2112-07-24
# Timezone: US/Pacific
# Parsed date: 2112-07-24
# ISO week number:
# 2112-W30

wn 2112-07-24
# 2112-W30

wn --last
# 2023-W48
```

## TEST
* its a cli service that echoes to stdout
* use `capsys` fixture as in `test_wn` to compare outputs to expected

```sh
just test tests/wn

            ✙✙✙✙✙✙✙✙    TESTING    ✙✙✙✙✙✙✙✙
poetry run pytest --disable-warnings --verbose tests/wn
========================================================= test session starts ==========================================================
rootdir: /Users/merlinr/repo/the-others/desertislandutils
collected 1 item
tests/wn/test_wn.py::test_wn_options PASSED                                                                                      [100%]
```

## DEPLOYMENT
Pull request has automatic checks on github actions.

https://github.com/mahiki/desertislandutils/pull/7
Need up update, local package is on python 3.11, yaml has 3.9

https://typer.tiangolo.com/tutorial/package/

[PR 7: Deployed CICD passing, automatically merged](https://github.com/mahiki/desertislandutils/pull/7)

[**Looks like I'm not using PyPi**](https://pypi.org/project/desertislandutils/) on v0.1.0

[V0.2.1 Homebrew tap mahiki](https://github.com/mahiki/homebrew-tap) release was 2022-08-02


## DOCS
```sh
pipx install typer-cli

typer 
```