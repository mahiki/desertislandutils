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
  @echo "   {{BCY}}Workflow to develop python scripts and deploy via uv tool{{NC}}"
  @echo
  @echo "       {{CY}}1.{{NC}} Develop/commit on dev"
  @echo "       {{CY}}2.{{NC}} just test"
  @echo "       {{CY}}3.{{NC}} just bump"
  @echo "       {{CY}}4.{{NC}} git checkout -b release/x.y.z"
  @echo "           {{CY}}*{{NC}} final TESTS and debug"
  @echo "           {{CY}}*{{NC}} git push --set-upstream origin release/x.y.z"
  @echo "           {{CY}}*{{NC}} PR 'release/x.y.z' for CI/CD tests (click link to open PR)"
  @echo "           {{CY}}*{{NC}} debug GHA tests"
  @echo "           {{CY}}*{{NC}} GHA-bot auto-merge to main and tag"
  @echo "       {{CY}}5.{{NC}} Publish to PyPI: uv publish"
  @echo "       {{CY}}6.{{NC}} Install globally: uv tool install desertislandutils"
  @echo "       {{CY}}7.{{NC}} git delete that release branch or maybe GHA does for you"
  @echo
  @echo "   {{BCY}}Running utils in uv environment{{NC}}"
  @echo
  @echo "       {{GR}}just uv wn"
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
