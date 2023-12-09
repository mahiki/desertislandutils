# Pytest example: using temporary test directory
#
#   poetry run pytest --capture=no ./tests/test_unit.py
#   pytest --capture=no ./tests/test_unit.py

import pytest
import os

# test that pytest tmp directory is empty
# use the system tmp directory base in a test
def test_unit(tmp_path):
    tmp_dir = tmp_path
    system_temp = os.environ['TMPDIR']

    print("\n\tsystem tmp directory: {}".format(system_temp))
    print("\n\ttmp_path for this test run: {}".format(tmp_dir))

    assert len(os.listdir(tmp_dir)) == 0
