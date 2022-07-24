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

## 4. RELEASE
pull branch, bump version, push
```sh
git checkout -b release/0.2.0 dev
./bump-version.sh 0.2.0
git commit -a -m "tests passed, version bumped 0.2.0, ready for local usage test"

git push --set-upstream origin release/0.2.0
# GITHUB MESSAGE
# remote: Create a pull request for 'release/0.2.0' on GitHub by visiting:
# remote:      https://github.com/mahiki/desertislandutils/pull/new/release/0.2.0
```

So new PR is automatically created for a 'release' branch pushed to remove

### PASS:test local release version in real usage
```bash
# from desertislandtils
poetry shell
# /Users/segovia/Library/Caches/pypoetry/virtualenvs/desertislandutils-AVSNhiuH-py3.9

ls /Users/segovia/Library/Caches/pypoetry/virtualenvs/desertislandutils-AVSNhiuH-py3.9/bin/too
# This is the executable made on 2022-03-18
# I need to build the new executable, or

cd "/Users/segovia/andromeda/house/selling-stuff"
python /Users/segovia/repo/python-dev/desertislandutils/src/toobigdatadoc/too.py --help

ls -l doc/
# lrwxr-xr-x 1  45 Jul  8 11:37 doc -> ../../../toodoc/andromeda/house/selling-stuff

mv doc dc
python /Users/segovia/repo/python-dev/desertislandutils/src/toobigdatadoc/too.py doc
unlink dc

# new doc/ points to same toodoc folder as the relative one
ls -l
lrwxr-xr-x 1  51 Jul 22 13:39 doc -> /Users/segovia/toodoc/andromeda/house/selling-stuff
# PASS
```

### test from built wheel and executable
```py
z desertislandutils
poetry build --format wheel
# Building desertislandutils (0.2.0)
#   - Building wheel
#   - Built desertislandutils-0.2.0-py3-none-any.whl

l dist
# Mar 17 14:33 desertislandutils-0.1.0-py3-none-any.whl
# Mar 17 14:33 desertislandutils-0.1.0.tar.gz
# Jul 22 13:53 desertislandutils-0.2.0-py3-none-any.whl

# no tar.gz was made, and this file is unchanged
ls -l /Users/segovia/Library/Caches/pypoetry/virtualenvs/desertislandutils-AVSNhiuH-py3.9/bin/too
```

Where to find my steps for creating tarball and homebrew deployment?
see `create-a-homebrew-tap.md`

```sh
# previously I did this
brew create --python --tap mahiki/tap https://files.pythonhosted.org/packages/62/0f/db9abf3d5d7513b50f618d634cf666278cd6deb0e73f5880bfcc838b5c59/desertislandutils-0.1.0.tar.gz

```

----------
## RSRC
[poetry docs](https://python-poetry.org/docs/cli/#install)