"""A command line utility to create a symlinked folder in the current directory, pointing to the 'too' project root directory.

For the purpose of keeping source code and notes as text files, with associated documents, data, and images stored separately on a parallel file structure. The main benefits are browsing through directories and scanning the notes contents visually, and looking through filenames without a lot of clutter.

NOTE: git repos can be moved anywhere, because their path is uniquely definied by root name.

Usage:

too big|data|doc
"""
# TODO: [--verbose, -v] version print 
#   folder created: $HOME/toodoc/datasci/biq/biq-206/bigtest
#   symlink:        doc -> $HOME/toodoc/datasci/biq/biq-206/bigtest

from argparse import ArgumentParser
from git import Repo, exc
from pathlib import Path

POSITIONAL_ARGS = {
    'big': 'toobig'
    , 'data': 'toodata'
    , 'doc': 'toodoc'
    }

def cli_parser(args = None):
    if args: args = [args]       # must do for test calls
    arg_choices = list(POSITIONAL_ARGS)
    parser = ArgumentParser(
        prog = "too"
        , description = "Create symlinked parallel folders under HOME/{toobig|toodata|toodoc}, to contain data/binary files outside of\n git repo or away from source/text files."
        )
    parser.add_argument(
        'too_dir'
        , choices = arg_choices
        , help = "large files to exclude from backup, smallish datasets, binary files like pdf"
        )
    args = parser.parse_args(args)
    return args.too_dir

def is_git_repo(path):
    try:
        _ = Repo(path, search_parent_directories=True)
        return True
    except exc.InvalidGitRepositoryError:
        return False

def repo_root(repo_path):
    try:
        repo = Repo(repo_path, search_parent_directories=True)
        return Path(repo.working_tree_dir)
    except exc.InvalidGitRepositoryError:
        return None

def top_dir_path(tbdd):
    topname = POSITIONAL_ARGS.get(tbdd, "ERROR")
    return Path.home() / topname

def make_topdir_and_link(new_path):
    try:
        new_path.mkdir(parents=True, exist_ok=True)
    except:
        print("Could not make TooPath directory.")
    try:
        Path(TOPDIR_NAME).symlink_to(new_path)
    except FileExistsError:
        print("Symlink already exists")

def too_path(any_path):
    if is_git_repo(any_path):
        repo_root_path = repo_root(any_path)
        path_from_root = any_path.relative_to(repo_root_path)
        return top_dir_path(TOPDIR_NAME) / repo_root_path.name / path_from_root
    else:
        path_from_home = any_path.relative_to(Path.home())
        return top_dir_path(TOPDIR_NAME) / path_from_home


def main(too_dir = None):
    global TOPDIR_NAME

    too_dir = cli_parser(too_dir)
    TOPDIR_NAME = too_dir

    make_topdir_and_link(too_path(Path.cwd()))

if __name__ == "__main__":
    main()
