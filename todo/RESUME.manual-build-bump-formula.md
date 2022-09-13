# RESUME Automation Work From this Point
>I need to get back to my day job for now

Completed:
* merge releases
* tag
* merge back to dev

TODO:

* poetry build and create release
* upload built tar.gz to github release tag
* edit mahiki/homebrew-tap with new URL and SHA
* prompt for delete release branch

## TODO: MANUAL BUILD STEPS TO AUTOMATE
```sh
# cd  ../desertislandtils
git checkout tag v0.2.1
poetry run pytest       # DEFINITELY INCLUDE THIS IN WORKFLOW
poetry build --format sdist
    # Building desertislandutils (0.2.1)
    #   - Building sdist
    #   - Built desertislandutils-0.2.1.tar.gz

############## MANUAL UPLOAD ###########################################################
# MANUALLY UPLOAD TO GITHUB RELEASE TAG v0.2.1
########################################################################################
curl -Ls \
    https://github.com/mahiki/desertislandutils/releases/download/v0.2.1/desertislandutils-0.2.1.tar.gz \
    | shasum -a 256
# e7e31e37a4073382a0be4ac8410b41117671700cc4aa9e17cf43a2d06bfd5625

brew edit mahiki/tap/desertislandutils
# edit URL
# edit SHA

cd /repo/homebrew-tap

git tag --annotate v0.2.1 -m

################ NOTE: YOU MAY HAVE TO REBUILD WITH brew #################################
# If your project dependencies change then the brew pr-pull workflow may be needed,
# or brew create workflow.
##########################################################################################

# now the new version should be available
brew upgrade desertislandutils
    # ==> Upgrading 1 outdated package:
    # mahiki/tap/desertislandutils 0.1.0 -> 0.2.1
    # ..
    # ==> Downloading https://github.com/mahiki/desertislandutils/releases/download/v0.2.1/desertislandutils-0.2.1.tar.gz
    # ==> Downloading from https://objects.githubusercontent.com/github-production-release-asset-2e65be/467741670/6203a243-4d19-4109-9abe-9
    # ######################################################################## 100.0%
    # ==> Upgrading mahiki/tap/desertislandutils
    #   0.1.0 -> 0.2.1
    # ..
    # ==> Installing mahiki/tap/desertislandutils dependency: python@3.9
    # ==> Pouring python@3.9--3.9.13_1.arm64_monterey.bottle.tar.gz
    # ==> /opt/homebrew/Cellar/python@3.9/3.9.13_1/bin/python3 -m ensurepip
    # ==> /opt/homebrew/Cellar/python@3.9/3.9.13_1/bin/python3 -m pip install -v --no-deps --no-index --upgrade --isolated --target=/opt/ho
    # 🍺  /opt/homebrew/Cellar/python@3.9/3.9.13_1: 3,088 files, 57.6MB
    # ==> Installing mahiki/tap/desertislandutils
    # ==> python3.9 -m venv --system-site-packages /opt/homebrew/Cellar/desertislandutils/0.2.1/libexec
    # ==> /opt/homebrew/Cellar/desertislandutils/0.2.1/libexec/bin/pip install -v --no-deps --no-binary :all: --ignore-installed /private/t
    # ==> /opt/homebrew/Cellar/desertislandutils/0.2.1/libexec/bin/pip install -v --no-deps --no-binary :all: --ignore-installed /private/t
    # ==> /opt/homebrew/Cellar/desertislandutils/0.2.1/libexec/bin/pip install -v --no-deps --no-binary :all: --ignore-installed /private/t
    # ==> /opt/homebrew/Cellar/desertislandutils/0.2.1/libexec/bin/pip install -v --no-deps --no-binary :all: --ignore-installed /private/t
    # 🍺  /opt/homebrew/Cellar/desertislandutils/0.2.1: 1,719 files, 19.1MB, built in 19 seconds

brew info mahiki/tap/desertislandutils
    # mahiki/tap/desertislandutils: stable 0.2.1
    # Be here, thy collection of personal convenience utilities
    # https://github.com/mahiki/homebrew-tap
    # /opt/homebrew/Cellar/desertislandutils/0.2.1 (1,719 files, 19.1MB) *
    #   Built from source on 2022-08-02 at 08:58:17

mcd desertislandutils
too big
ls -la
lrwxr-xr-x 1 55 Aug  2 09:25 big -> /Users/segovia/toobig/trashwork/tests/desertislandutils
```

### DONE