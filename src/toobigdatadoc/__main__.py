"""Create a symlinked folder in the current directory pointing to 'too' project root directory.

I like to keep source code and notes as text files, with associated documents, data, and images stored separately on a parallel file structure. The main benefits are browsing through directories and scanning the notes contents visually, and looking through filenames without a lot of clutter.

Usage:
          
too big|data|doc
"""

from argparse import ArgumentParser
from git import Repo
from pathlib import Path, PosixPath

def is_git_repo(path):
    try:
        _ = Repo(path, search_parent_directories=True)
        return True
    except exc.InvalidGitRepositoryError:
        return False

def get_repo_root(path):
    try:
        repo = Repo('.', search_parent_directories=True)
        return Path(repo.working_tree_dir)
    except exc.InvalidGitRepositoryError:
        return None

def top_dir_path(tbdd):
    switch = {
        'big': "toobig"
        , 'data': "toodata"
        , 'doc': "toodoc"
        }
    top_path = Path.home() / switch.get(tbdd, "Input must be member of {big,data,doc}")
    return top_path

def parse_cli_args():
    parser = ArgumentParser(
            prog = "too"
            , description = "Create symlinked parallel folders to contain data/binary files outside of\n git repo or away from source/text files."
        )

    parser.add_argument(
        'topdir'
        , choices = ['big', 'data', 'doc']
        , help = "large files to exclude from backup, smallish datasets, binary files like pdf"
        )
    args = parser.parse_args()

    print("top_dir_arg: {}".format(args.topdir))
    return args.topdir

def main():
    topdir = parse_cli_args()

    if is_git_repo(Path.cwd()):
        repo_root = get_repo_root(Path.cwd())
        path_from_root = Path.cwd().relative_to(repo_root)
        too_path = top_dir_path(topdir) / repo_root.name / path_from_root
    else:
        pass
        # this will be $HOME/top_dir_path/relative_path_from_cwd_to_home

    try:
        too_path.mkdir(parents=True, exist_ok=True)
        Path(topdir).symlink_to(too_path)
    except:
        print("TooPath and Link creation had problems.")

    print("TOO: you have successfully called the command line. New path to create is:")
    print(str(too_path))

    
if __name__ == "__main__":
    main()
