# CICD Notes
Notes on current configuration of CICD.

## CURRENT WORKFLOW
* on push branch `release/**` trigger
* tests
* merge branch
* git tag
* merge back to dev


## MORE STEPS
1. Build artifact
2. Generate a release
3. trigger mahiki/homebrew-tap

```sh
poetry version --short
# 0.3.0

poetry build --format sdist
# desertislandutils-0.3.0.tar.gz
poetry build
# also makes desertislandutils-0.3.0-py3-none-any.whl


```

### Create Release
#### gh release create
This one looks pretty simple

```sh
gh release create v1.2.3 --generate-notes ./dist/*
```

#### Poetry uses ncipollo/release-action@v1
Looks good, poetry is tight, and generates notes too.
[poetry repo workflow](https://github.com/python-poetry/poetry/blob/master/.github/workflows/release.yml)

```yaml
name: Releases

on: 
  push:
    tags:
    - '*'

jobs:

  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
    - uses: actions/checkout@v3
    - uses: ncipollo/release-action@v1
      with:
        artifacts: "dist/*"
        bodyFile: "body.md"
        generateReleaseNotes: true
# bodyFile not needed if auto generating notes.
```

## OPTIONAL ADDITIONS
Prerelease actions are available with examples of various approaches.
[marvinpinto/actions release](https://github.com/marvinpinto/action-automatic-releases)
