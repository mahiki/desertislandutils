# test command line arg handling, help function, and core functions

import pytest
import os

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
