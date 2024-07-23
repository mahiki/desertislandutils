# TODO
* build and bump homebrew: justfile or github actions?
* tests in GHA is cool, esp merge after tests pass

## TODO: ADD TEST FOR BUILD/DEPLOY
Homebrew calls each script like the following. Its possible the deployed script can fail because of misconfiguration in the pyproject file.
So its smart to run a test of the built package by building in CICD `brew install desertislandutils.rb` or something.

```sh
# /opt/homebrew/bin/wn
#!/opt/homebrew/Cellar/desertislandutils/0.3.9/libexec/bin/python
# -*- coding: utf-8 -*-
import re
import sys
from src.weeknumber.wn import app
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(app())
```

## TODO: GHA AUTOMATION: WHAT?
Goals are what?

1. test on push
2. ready for release -> somehow -> merge and tag
3. delete release branch
4. merge main back into dev
5. generate a release on the gh releases page from main tag
6. build executable for homebrew
7. bump homebrew formula
    * trigger brew repo `mahiki/tap/desertislandutils` to link new version


I mean, right now 'Merge Release Branch and Tag' runs every time you push a release branch that passes tests.
I guess push feature branch, then checkout the release branch only when ready to release.
Maybe I should only trigger on merge to release branch? i dunno

## TODO: JUSTFILE
add to justfile the merge/release process. Merge and tag GHA only happens for 
branch with release/v...
test runs with everything pretty much
release will happen after successful release merge.
so work flow is:
dev .. do work
or feature-branch
then checkout dev or feature to new release/x.x.x
once test passes on a release branch its auto-merging.

maybe a better way is auto-merge and tag after dev push or something

Also, NOTE that GHA actions changes should be worked on in main. its own thing.

### Release could be a jusftfile action
https://github.com/github-release/github-release

    github-release release \
        --user aktau \
        --repo gofinance \
        --tag v0.1.0 \
        --name "the wolf of source street" \
        --description "Not a movie, contrary to popular opinion. Still, my first release!" \
        --pre-release
    
    github-release upload \
        --user aktau \
        --repo gofinance \
        --tag v0.1.0 \
        --name "gofinance-osx-amd64" \
        --file bin/darwin/amd64/gofinance