"""Create a symlinked folder in the current directory pointing to 'too' project root directory.

I like to keep source code and notes as text files, with associated documents, data, and images stored separately on a parallel file structure. The main benefits are browsing through directories and scanning the notes contents visually, and looking through filenames without a lot of clutter.

Usage:
          
too big|data|doc
"""

import argparse
from pathlib import Path

TOO_BIG_LOCATION = Path.home() / "toobig"
TOO_DATA_LOCATION = Path.home() / "toodata"
TOO_DOC_LOCATION = Path.home() / "toodoc"

def main():
    parser = argparse.ArgumentParser(
        prog = "too"
        , description = "Create symlinked parallel folders to contain data/binary files outside of\n git repo or away from source/text files."
    )

    parser.add_argument(
        'topdir'
        , choices= ['big', 'data', 'doc']
        , help = "large files to exclude from backup, smallish datasets, binary files like pdf"
        )

    args = parser.parse_args()
    print("arg1: {}".format(args.topdir))
    print("name: {}".format(__name__))
    print("TOO: you have successfully called the command line. Goodbye.")

if __name__ == "__main__":
    main()
