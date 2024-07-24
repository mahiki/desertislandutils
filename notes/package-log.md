# Package desertislandutils Log
>starting an actual log


## 2024-07-23: POETRY PLUGIN HOMEBREW-FORMULA
I think this is to solve the way install is a little different than virtualenv or pip install build things.

```sh
git checkout -b feature/po-brew-form
pipx inject poetry poetry-homebrew-formula
poetry homebrew-formula --help
    # Generating formula

    # No valid link found for desertislandutils.
```
Well, that was fun

## 2024-07-22: GHA Working finally
*  `release.yml` is working on tag `v0.3.9` 
*  good to go with pushing `release/*` tags
*  update the homebrew formula and we are in heaven

TODO: brew is still a manual thingy
* It looks like homebrew-tap has a tagged commit for last one
* How do I indicate the version? It just takes from tag?
    * cloudflare warp used `version '2023.8.2'` command
* Actually, since it builds from source maybe it gets it from the poetry package.

**Actually:** `Error: Stable: version 0.3.9 is redundant with version scanned from URL`
Test-bot style checks: spacing in yml, and version info not needed.

```sh
# https://github.com/mahiki/desertislandutils/releases/tag/v0.3.9
# https://github.com/mahiki/desertislandutils/releases/download/v0.3.9/desertislandutils-0.3.9.tar.gz

vLatest='https://github.com/mahiki/desertislandutils/releases/download/v0.3.9/desertislandutils-0.3.9.tar.gz'
curl -Ls $vLatest  | shasum -a 256
# d71e44f9306fe2833664c74ab07690913eeb460d0f84dbc2ee1fb8ebbaf58032  -

# update file in 
# https://github.com/mahiki/homebrew-tap/blob/main/Formula/desertislandutils.rb
code ./homebrew-tap/Formula/desertislandutils.rb

brew audit desertislandutils
# nothing

brew edit desertislandutils
    # this just opens the local file /opt/homebrew/Library/Taps/mahiki/homebrew-tap/Formula/desertislandutils.rb

brew developer off

git add .; git commit -m "Release v0.3.9"
git tag -a v0.3.9 -m "v0.3.9 matching release of desertisland utils"
git push --tags

# fix test-bot GHA actions
git add .; git commit -m 'fixes'
```

The test-bot things keep failing, but whatever its for syntax in markdown files.

### Moment of Truth
```sh
brew update
    # ==> Updating Homebrew...
    # Updated 1 tap (mahiki/tap).
brew upgrade desertislandutils

brew info desertislandutils
    # ==> mahiki/tap/desertislandutils: stable 0.3.9
    # /opt/homebrew/Cellar/desertislandutils/0.2.1 (109 files, 828.6KB) *
    # ERROR: Package 'desertislandutils' requires a different Python: 3.9.19 not in '<4.0,>=3.11'

wn --help
```
DAMMIT!

    depends_on "python@3.9" -> depends_on "python@3.11"

Also: literally fixing indentation in a markdown file, cant get it to ignore

```sh
brew update
brew upgrade desertislandutils
    # ==> Upgrading 1 outdated package:
    # mahiki/tap/desertislandutils 0.2.1 -> 0.3.9

wn --help
    # Traceback (most recent call last):
    # File "/opt/homebrew/bin/wn", line 5, in <module>
    #     from src.weeknumber.wn import app
    # ModuleNotFoundError: No module named 'src.weeknumber'

bat /opt/homebrew/bin/wn
    #!/opt/homebrew/Cellar/desertislandutils/0.3.9/libexec/bin/python
    # -*- coding: utf-8 -*-
    import re
    import sys
    from src.weeknumber.wn import app
    if __name__ == '__main__':
        sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
        sys.exit(app())

# AHA! the pyproject.toml:
packages = [
    { include = "src/toobigdatadoc" }
]

# this was there, prob why the poetry shell was working fine:
[tool.poetry.scripts]
too = "src.toobigdatadoc.too:main"
wn = "src.weeknumber.wn:app"
```

Looks like that needs update and fix.


### Poetry Creates its Own Executable Scripts
And Poetry creates an executable script as well in the virtual environment:
```sh
# bin/wn:
bat --style plain ~/Library/Caches/pypoetry/virtualenvs/desertislandutils-zyraM7-y-py3.12/bin/wn
#!~/Library/Caches/pypoetry/virtualenvs/desertislandutils-zyraM7-y-py3.12/bin/python
import sys
from src.weeknumber.wn import app

if __name__ == '__main__':
    sys.exit(app())

# bin/too:
bat --style plain ~/Library/Caches/pypoetry/virtualenvs/desertislandutils-zyraM7-y-py3.12/bin/too
#!~/Library/Caches/pypoetry/virtualenvs/desertislandutils-zyraM7-y-py3.12/bin/python
import sys
from src.toobigdatadoc.too import main

if __name__ == '__main__':
    sys.exit(main())
```

### So what is this `--no-root` business?
```sh
cd "$(mktemp -d)"
curl -LO https://github.com/mahiki/desertislandutils/releases/download/v0.3.10/desertislandutils-0.3.10.tar.gz
tar -xf
cd desertislandutils-0.3.10
poetry install --no-root
    # Creating virtualenv desertislandutils-vB0CMQFH-py3.12 in ~/Library/Caches/pypoetry/virtualenvs
    # installs all dependencies
l ~/Library/Caches/pypoetry/virtualenvs/desertislandutils-vB0CMQFH-py3.12/bin
# NOPE
# There is no executable script call for each poetry thing.
```