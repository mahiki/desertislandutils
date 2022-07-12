# desertislandutils
Refactoring my convenience utility bash scripts into python for learning and profit.

* build: poetry
* deploy: poetry -> pypi -> homebew
* github CI actions

## SCRIPTS
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
