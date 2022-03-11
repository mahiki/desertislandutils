"""Create a symlinked folder in the current directory pointing to 'too' project root directory.

I like to keep source code and notes as text files, with associated documents, data, and images stored separately on a parallel file structure. The main benefits are browsing through directories and scanning the notes contents visually, and looking through filenames without a lot of clutter.

Usage:
          
too big|data|doc
"""

from argparse import ArgumentParser
from git import Repo
from pathlib import Path

def call_the_parser():
    parser = ArgumentParser(
            prog = "too"
            , description = "Create symlinked parallel folders to contain data/binary files outside of\n git repo or away from source/text files."
        )

    parser.add_argument(
        'arg1'
        , choices = ['big', 'data', 'doc']
        , help = "large files to exclude from backup, smallish datasets, binary files like pdf"
        )

    args = parser.parse_args()

    return args.arg1

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

def top_dir_rel_path(tbdd):
    switch = {
        'big': 'toobig'
        , 'data': 'toodata'
        , 'doc': 'toodoc'
        }
    topname = switch.get(tbdd, "ERROR")
    relative_path_home = str(Path.cwd().relative_to(Path.home()))
    levels_home = len(relative_path_home.split('/'))
    dots_home = '../' * levels_home

    return Path(dots_home) / topname

def make_topdir_and_link(topdir_choice, new_path):
    try:
        new_path.mkdir(parents=True, exist_ok=True)
    except:
        print("Could not make TooPath directory.")
    try:
        Path(topdir_choice).symlink_to(new_path)
    except FileExistsError:
        print("Symlink already exists")

def too_rel_path(any_path):
    if is_git_repo(any_path):
        repo_root_path = repo_root(any_path)
        path_from_root = any_path.relative_to(repo_root_path)
        return top_dir_rel_path(topdir_name) / repo_root_path.name / path_from_root
    else:
        path_from_home = any_path.relative_to(Path.home())
        return top_dir_rel_path(topdir_name) / path_from_home


def main():
    topdir_name = call_the_parser()

    make_topdir_and_link(topdir_name, too_rel_path(Path.cwd()))
    
if __name__ == "__main__":
    main()
