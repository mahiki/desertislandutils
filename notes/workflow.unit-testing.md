# Poetry, Pytest, and Environment
* I want to toobigdatadoc test to create folders in a test enviroment
* Mock the environment to change `Path.home()`
* Tests will create too/big/data folders in a system temp folder location

This describes setting enviroment variables:
https://adamj.eu/tech/2020/10/13/how-to-mock-environment-variables-with-pytest/

pytest docs on monkeypatch:
https://docs.pytest.org/en/7.1.x/how-to/monkeypatch.html

pytest requesting temporary directories
https://doc.pytest.org/en/latest/getting-started.html

## WHAT IT LOOKS LIKE
```sh
poetry run pytest -q
# quiet output

poetry run pytest  -v

poetry run pytest --captures=no
```

# test_pytest
## TESTING MORE NOTES
* incorporate poetry, this is your environment manager
* pytest is probably good, `poetry add pytest`, `poetry install`
* `poetry run pytest tests/`
* [note where poetry project keeps pytest as a dev-dependency](https://github.com/python-poetry/poetry/blob/master/pyproject.toml)

[**Conventions for pytest discovery**](https://docs.pytest.org/en/latest/explanation/goodpractices.html#test-discovery)

[here is SO poetry and pytest](https://stackoverflow.com/questions/61783925/running-a-package-pytest-with-poetry)
[pytest getting started](https://doc.pytest.org/en/latest/getting-started.html)

## TEST_PYTEST.PY STEPS
### BASIC PYTEST
* using `test_sysexit.py`
* https://docs.pytest.org/en/7.1.x/getting-started.html

```sh
poetry run pytest tests/toobigdatadoc/test_pytest.py
# PASSES
```

### TEMPORARY TEST FOLDERS
[pytest temp folders](https://docs.pytest.org/en/7.1.x/how-to/tmp_path.html)

```python
# test_too.py
import pytest

def test_needsfiles(tmp_path):
    print(tmp_path)
    assert 0

# at shell ~/.../desertislandutils
$> poetry run pytest -v --captures=no
# ----------------------------------------------- Captured stdout call -----------------------------------------------
# /private/var/folders/sq/4qxp1j7x2jv5c18qty294kfm0000gn/T/pytest-of-segovia/pytest-3/test_needsfiles0
```

So the temporary folder works, and it persists after the test is done

### DELETING TEMP FOLDERS
* no need to delete, only the last 3 are saved on system common `/tmp` folder
* place cleanup resources commands after `yield` from functions