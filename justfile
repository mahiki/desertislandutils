import './base.justfile'
set positional-arguments := true

# just --list
[private]
default:
  @just --list --unsorted --list-heading $'Poetry development workflow commands:\n'

# 'poetry run' pass thru command
po *args:
  @poetry run "$@"

# pass thru
pass *args:
  {{args}}

# ptpython REPL in poetry shell
repl:
  @poetry run ptpython

# instructions to bump version number
bump:
  @echo
  @echo "   {{BCY}}REMINDER:{{NC}} You need to manually bump the version numbers in these locations."
  @echo "       ./desertislandutils/"
  @echo "           {{YW}}__init__.py"
  @echo "           pyproject.toml"
  @echo "           tests/test_desertislandutils.py{{NC}}"
  code __init__.py pyproject.toml tests/test_desertislandutils.py

# pytest
test *args:
  @echo
  @echo "            ✙✙✙✙✙✙✙✙    TESTING    ✙✙✙✙✙✙✙✙"
  poetry run pytest --disable-warnings --verbose {{args}}

# INFO: develop, build, deploy
info:
  @echo
  @echo "   {{BCY}}Workflow to develop python scripts and deploy to homebrew{{NC}}"
  @echo
  @echo "       {{CY}}1.{{NC}} Develop/commit on dev"
  @echo "       {{CY}}2.{{NC}} just test"
  @echo "       {{CY}}3.{{NC}} just bump"
  @echo "       {{CY}}4.{{NC}} git checkout -b release/0.3.1"
  @echo "           {{CY}}*{{NC}} final TESTS and debug"
  @echo "           {{CY}}*{{NC}} git push --set-upstream origin release/0.3.1"
  @echo "           {{CY}}*{{NC}} PR 'release/0.3.1' for CI/CD tests (click link to open PR)"
  @echo "           {{CY}}*{{NC}} debug GHA tests"
  @echo "           {{CY}}*{{NC}} GHA-bot auto-merge to main and tag"
  @echo "       {{CY}}5.{{RD}} TODO:{{NC}} release to homebrew repo on merge to main"
  @echo "       {{CY}}6.{{NC}} git delete that release branch or maybe GHA does for you"
  @echo 
  @echo "   {{BCY}}Running utils in poetry environment{{NC}}"
  @echo 
  @echo "       {{GR}}just po wn"
  @echo "       {{GR}}just po wn --help"
  @echo "       {{GR}}just po too --help"
  @echo "       {{GR}}just po too --help"
  @echo
  @echo "       {{BBK}}# or directly from poetry shell:{{NC}}"
  @echo "       {{GR}}poetry shell"
  @echo "       {{BGR}}wn --help"
  @echo
  
