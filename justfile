YW := '\033[0;33m'
RD := '\033[0;31m'
LC := '\033[0;36m'
LB := '\033[0;34m'
LG := '\033[0;32m'
NC := '\033[0m'

# just --list
default:
  @just --list --unsorted

# INFO: develop, build, deploy
info:
  @echo
  @echo "   {{LC}}Workflow to develop python scripts and deploy to homebrew.{{LG}}"
  @echo
  @echo "       Develop and commit on dev, pull feature branch."
  @echo "       Commit incrementally."
  @echo "       Make tests, test."
  @echo "       Push branch."
  @echo "       version, tag, push, ...?."
  @echo "       4. finalize dev commits, pull release branch release/0.2.0"
  @echo "           * final TESTS and debug"
  @echo "           * bump version"
  @echo "           * PR 'release/0.2.0' for CI/CD tests"
  @echo "           * merge to main"
  @echo "           * tag"
  @echo "       5. release to homebrew repo on merge to main"


# ptpython REPL in poetry shell
repl:
  @poetry run ptpython

# instructions to bump version number
bump:
  @echo
  @echo "   {{LC}}REMINDER:{{NC}} You need to manually bump the version numbers in these locations."
  @echo "       ./desertislandutils/"
  @echo "           {{YW}}__init__.py"
  @echo "           pyproject.toml"
  @echo "           tests/test_desertislandutils.py"

# pytest
test *args:
  @echo
  @echo "            ✙✙✙✙✙✙✙✙    TESTING    ✙✙✙✙✙✙✙✙"
  poetry run pytest --disable-warnings --verbose {{args}}
