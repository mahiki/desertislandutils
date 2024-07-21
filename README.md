# desertislandutils
Refactoring my convenience utility bash scripts into python for learning and profit. Deployed for MacOS via homebrew, its really far better than shell scripting, yuck!

## INSTALL
    brew install mahiki/tap/desertislandutils

## THE UTILS
### toobigdatadoc
I like to keep text files in one directory system, with supporting data files and binary documents in parallel directories from the home folder: `toobig`, `toodata`, `toodoc`. For example, its easy to exclude the whole `toobig` directory structure from backups, since there is nothing but huge files here.

    $HOME
        |-- toobig
            |-- # replicated folder paths with large files here, assume not to be backed up
        |-- toodata
            |-- # small-ish data files in support of the parallel root
        |-- toodoc
            |-- # usually pdfs or image files

```sh
$> too --help
usage: too [-h] {big,data,doc}

Create symlinked parallel folders to contain data/binary files outside of git repo or away from source/text files.

positional arguments:
  {big,data,doc}  large files to exclude from backup, smallish datasets, binary files like pdf

optional arguments:
  -h, --help      show this help message and exit
Kehena segovia: ~
```

### weeknumber
```sh
wn --help

 Usage: wn [OPTIONS] [DATE]

 ISO year week number of a date as YYYY-WDD. Default weekend day is Sat.
 Example:
 $> wn 'Jul 22'
 2023-W29

╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────────╮
│   date      [DATE]  A text expression of date, ex: 'November 27', or 2112-07-29 [default: (dynamic)]          │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --sunday                     Weekend is Saturday by default, this flag sets Sunday weekend day.               │
│ --last                       Give week number of most recently completed week (overrides DATE argument).      │
│ --verbose       --no-verbose [default: no-verbose]                                                            │
│ --install-completion         Install completion for the current shell.                                        │
│ --show-completion            Show completion for the current shell, to copy it or customize the installation. │
│ --help                       Show this message and exit.                                                      │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

----------
## DEVELOPMENT
>Trying to automate the merge tag homebrew tap repo upgrade thing. Its not going great.

* build: poetry
* deploy: poetry -> pypi -> homebrew
* github CI actions

### JUSTFILE
>Best documentation is in the Just taskrunner `justfile`.

```sh
just info

just wn --help

# also direct into poetry environment
poetry shell
(desertislandutils)> wn --help
```

### Testing
    just test
