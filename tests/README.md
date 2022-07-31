# Poetry Tests with Pytest
* `tmp_path` is an imported fixture
* note the args handling of CLI calls vs. test function calls `[args]` with `argparse`
* `from desertislandutils.src.toobigdatadoc import too` brings module object into scope
  
```py
# repo/python-dev/pytest/tests/test_unit.py

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
```

```sh
poetry run pytest --capture=no tests/test_unit.py

# ==================================== test session starts =====================================
# platform darwin -- Python 3.9.10, pytest-7.1.2, pluggy-1.0.0
# rootdir: /Users/segovia/repo/python-dev/desertislandutils
# collected 1 item

# tests/test_unit.py
# 	system tmp directory: /var/folders/sq/4qxp1j7x2jv5c18qty294kfm0000gn/T/

# 	tmp_path for this test run: /private/var/folders/sq/4qxp1j7x2jv5c18qty294kfm0000gn/T/pytest-of-segovia/pytest-17/test_unit0
# .
# ===================================== 1 passed in 0.00s ======================================
```