# Publish Update to desertislandutils
I made a feature change in toobigdatadoc (absolute path not relative). Here is what I did to test and publish the update as a patch (minor)

## STEPS
1. git flow commits to dev
2. NODO: test functionality `too_py-test.sh`
    * `poetry run too --help` runs in the specified environment
    * `pytest` in the root directory all `test_*.py` files
3. TESTS: `poetry run pytest -v --captures=no
4. finalize dev commits, pull release branch 'release/0.2.0
    * final TESTS and debug
    * bump version
    * PR 'release/0.2.0' for CI/CD tests
    * merge to main
    * tag
5. release to homebrew repo on merge to main



[poetry docs](https://python-poetry.org/docs/cli/#install)