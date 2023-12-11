# just --list
default:
  @just --list --unsorted

# poetry pass thru command
po *args:
  poetry run {{args}}

# pass thru
blank *args:
  {{args}}

# INFO: develop, build, deploy
info:
  @echo
  @echo "   {{LC}}Workflow to develop python scripts and deploy to homebrew.{{LG}}"
  @echo
  @echo "       {{LG}}1.{{NC}} Develop/commit on dev"
  @echo "       {{LG}}2.{{NC}} just test"
  @echo "       {{LG}}3.{{NC}} just bump"
  @echo "       {{LG}}4.{{NC}} git checkout -b release/0.3.1"
  @echo "           * final TESTS and debug"
  @echo "           * git push --set-upstream origin release/0.3.1"
  @echo "           * PR 'release/0.3.1' for CI/CD tests (click link to open PR)"
  @echo "           * debug GHA tests"
  @echo "           * GHA-bot auto-merge to main and tag"
  @echo "       {{LG}}5.{{RD}} TODO:{{NC}} release to homebrew repo on merge to main"
  @echo 


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
  code __init__.py pyproject.toml tests/test_desertislandutils.py

# pytest
test *args:
  @echo
  @echo "            ✙✙✙✙✙✙✙✙    TESTING    ✙✙✙✙✙✙✙✙"
  poetry run pytest --disable-warnings --verbose {{args}}


BN := '\033[0;33m'
YW := '\033[1;33m'
RD := '\033[0;31m'
CY := '\033[0;36m'
LC := '\033[1;36m'
BL := '\033[0;34m'
LB := '\033[1;34m'
GN := '\033[0;32m'
LG := '\033[1;32m'
GY := '\033[0;37m'
NC := '\033[0m'
