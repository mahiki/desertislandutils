import './base.justfile'
set positional-arguments := true

# just --list
[private]
default:
  @just --list --unsorted --list-heading $'UV development workflow commands:\n'

# 'uv run' pass thru command
uv *args:
  @uv run "$@"

# pass thru
pass *args:
  {{args}}

# ptpython REPL in uv environment
repl:
  @uv run ptpython

# instructions to bump version number
bump level="patch":
  @echo
  @echo "   {{BCY}}Bumping version with {{YW}}uv version --bump [patch|minor|major]{{NC}}"
  @echo
  @uv version --bump {{ level }}

# pytest
test *args:
  @echo
  @echo "            ✙✙✙✙✙✙✙✙    TESTING    ✙✙✙✙✙✙✙✙"
  uv sync --all-extras
  uv run pytest --disable-warnings --verbose {{args}}

# INFO: develop, build, deploy
info:
  @echo
  @echo "   {{BCY}}Development workflow:{{NC}}"
  @echo
  @echo "       {{BBK}}1.{{NC}} Develop/commit on dev"
  @echo "       {{BBK}}2.{{NC}} just test"
  @echo "       {{BBK}}3.{{NC}} just bump"
  @echo "       {{BBK}}4.{{NC}} git checkout -b release/x.y.z"
  @echo "           {{BCY}}*{{NC}} final TESTS and debug"
  @echo "           {{BCY}}*{{NC}} git push --set-upstream origin release/x.y.z"
  @echo "           {{BCY}}*{{NC}} PR 'release/x.y.z' for CI/CD tests (click link to open PR)"
  @echo "       {{BBK}}CICD Handles:{{NC}}"
  @echo "           {{BCY}}*{{NC}} test package"
  @echo "           {{BCY}}*{{NC}} merge to main and tag"
  @echo "           {{BCY}}*{{NC}} publish to PyPI"
  @echo "       {{BBK}}5.{{NC}} git branch --merged main      {{WT}}# look for local branches to remove{{NC}}"
  @echo "       {{BBK}}6.{{NC}} git branch --delete release/x.y.z{{NC}}"
  @echo
  @echo "   {{BCY}}Running utils in uv environment{{NC}}"
  @echo
  @echo "       {{GR}}just uv wn --help"
  @echo "       {{GR}}just uv too --help"
  @echo

# sync dependencies
sync:
  uv sync

# sync with dev and test dependencies
sync-all:
  uv sync --all-extras

# build package
build:
  uv build

# install as global tool (from local source)
install-local:
  uv tool install --editable .

# uninstall global tool
uninstall:
  uv tool uninstall desertislandutils
