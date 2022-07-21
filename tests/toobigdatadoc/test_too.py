# test command line arg handling, help function, and core functions

import pytest
import os
from desertislandutils.src.toobigdatadoc import too

def test_main_help(capsys):
    help_args = [["-h"], ["--help"]]
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
    bad_input = ["42 -h poo"]
    expected_out = "too: error:"
    with pytest.raises(SystemExit) as pytest_wrapped_exception:
            too.main(bad_input)
    assert pytest_wrapped_exception.type == SystemExit
    captured = capsys.readouterr()
    assert expected_out in captured.err



# def test_unit(tmp_path):
#     tmp_dir = tmp_path
#     system_temp = os.environ['TMPDIR']

#     print("\n\tsystem tmp directory: {}".format(system_temp))
#     print("\n\ttmp_path for this test run: {}".format(tmp_dir))
#     print("\n\tcwd: {}".format(os.getcwd()))
#     print("\n\tchanging to TMPDIR/pytest_dir")
#     os.chdir(tmp_dir)
#     print("\n\tcwd: {}".format(os.getcwd()))

#     assert len(os.listdir(tmp_dir)) == 0
