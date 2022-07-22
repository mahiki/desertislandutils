# test command line arg handling, help function, and core functions

import pytest
import os
import git
from pathlib import Path
from desertislandutils.src.toobigdatadoc import too

def test_help(capsys):
    help_args = ["-h", "--help"]
    help_msg_part = "optional arguments:"

    for i in help_args:
        with pytest.raises(SystemExit) as pytest_wrapped_exception:
            too.main(i)
        assert pytest_wrapped_exception.type == SystemExit
        assert pytest_wrapped_exception.value.code == 0

        captured = capsys.readouterr()
        assert len(captured.err) == 0
        assert help_msg_part in captured.out

def test_bad_input(capsys):
    bad_input = "42 -h poo"
    expected_out = "too: error:"
    with pytest.raises(SystemExit) as pytest_wrapped_exception:
            too.main(bad_input)
    assert pytest_wrapped_exception.type == SystemExit
    captured = capsys.readouterr()
    assert expected_out in captured.err

def test_non_repo(tmp_path, monkeypatch):
    tmp_dir = tmp_path
    test_path_from_home = "non_repo_dir/subdir_1/subdir_2"

    monkeypatch.setenv("HOME", str(tmp_dir / "HOME"))
    test_home = Path.home()
    
    test_full_path = test_home / test_path_from_home
    Path.mkdir(test_full_path, parents=True)
    os.chdir(test_full_path)
    
    for i in iter(too.POSITIONAL_ARGS):
        too.main(i)

    # expected names created
    assert sorted(os.listdir(test_full_path)) == sorted(list(too.POSITIONAL_ARGS))

    # test link, dir existence
    for i in test_full_path.iterdir():
        assert i.is_symlink()
        assert i.is_dir()

    # read links, verify expected path from HOME
    for i in test_full_path.iterdir():
        too_path = i.readlink()
        too_stem = too_path.relative_to(test_home)
        too_stem_components = str(too_stem).split('/')
        too_stem_anchor = too_stem_components[0]
        assert too_stem_anchor in list(too.POSITIONAL_ARGS.values())

def test_git_repo(tmp_path, monkeypatch):
    tmp_dir = tmp_path
    git_repo_name = "git_repo_dir"
    test_path_from_home = git_repo_name + "/subdir_x/subdir_y"

    monkeypatch.setenv("HOME", str(tmp_dir / "HOME"))
    test_home = Path.home()
    
    test_full_path = test_home / test_path_from_home
    Path.mkdir(test_full_path, parents=True)
    git.Repo.init(test_home / git_repo_name)
    os.chdir(test_full_path)
    
    for i in iter(too.POSITIONAL_ARGS):
        too.main(i)

    # expected names created
    assert sorted(os.listdir(test_full_path)) == sorted(list(too.POSITIONAL_ARGS))

    # test link, dir existence
    for i in test_full_path.iterdir():
        assert i.is_symlink()
        assert i.is_dir()

    # read links, verify expected path from HOME
    for i in test_full_path.iterdir():
        too_path = i.readlink()
        too_stem = too_path.relative_to(test_home)
        too_stem_components = str(too_stem).split('/')
        too_stem_anchor = too_stem_components[0]
        assert too_stem_anchor in list(too.POSITIONAL_ARGS.values())
        assert too_stem_components[1] == git_repo_name
