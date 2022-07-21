# test command line arg handling, help function, and core functions

import pytest
import os
from desertislandutils.src.toobigdatadoc import too

def test_unit(tmp_path):
    tmp_dir = tmp_path
    system_temp = os.environ['TMPDIR']

    print("\n\tsystem tmp directory: {}".format(system_temp))
    print("\n\ttmp_path for this test run: {}".format(tmp_dir))
    print("\n\tcwd: {}".format(os.getcwd()))
    print("\n\tchanging to TMPDIR/pytest_dir")
    os.chdir(tmp_dir)
    print("\n\tcwd: {}".format(os.getcwd()))

    assert len(os.listdir(tmp_dir)) == 0


def test_main_help():
    help_args = ["-h", "--help"]
    help_msg_parts = ["positional arguments:"
        , "optional arguments:", "usage: too [-h] {big,data,doc}"]
    for i in help_args:
        with pytest.raises(SystemExit) as pytest_wrapped_exception:
            too.main([i])
        assert pytest_wrapped_exception.type == SystemExit
        assert pytest_wrapped_exception.value.code == 0
        # for j in help_msg_parts:
        #     assert j in resulted_stdout

# def test_main_invalid_args():
#  assert "Hello, Jakarta!" in result

#     captured = capsys.readouterr()
#     result = captured.out
#     expected = """\
# main arg toodir:  ['-h']
# usage: too [-h] {big,data,doc}

# Create symlinked parallel folders to contain data/binary files outside of git repo or away from source/text files.

# positional arguments:
#   {big,data,doc}  large files to exclude from backup, smallish datasets, binary files like pdf

# optional arguments:
#   -h, --help      show this help message and exit
# """

#     assert result == expected



## 1. test -h|--help argument input
# import toobigdatadoc somehow
# call it with argument liek from CLI


# CONTENT = "content"
# 
# def test_create_file(tmp_path):
    # d = tmp_path / "sub"
    # d.mkdir()
    # p = d / "hello.txt"
    # p.write_text(CONTENT)
    # assert p.read_text() == CONTENT
    # assert len(list(tmp_path.iterdir())) == 1
    # assert 0
