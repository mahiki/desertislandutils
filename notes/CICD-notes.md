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

### Example Gist: Lots of components of interest
https://gist.github.com/maxspahn/1e53f002bf504517c76b6fcbae9b36cc

#### Poetry uses ncipollo/release-action@v1
Looks good, poetry is tight, and generates notes too.
[poetry repo workflow](https://github.com/python-poetry/poetry/blob/master/.github/workflows/release.yml)

Output URL: (see release.yml)
    
    echo release URL: ${{ steps.create_release.outputs.html_url }}
    release URL: https://github.com/mahiki/desertislandutils/releases/tag/v0.3.9

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


### ACT local github actions runner
Justfile is keeping the docker host and container arch flag.
UGH. Problems with sockets, not macos images.... hopeless.

```sh
brew install act
# using Rancher Desktop in dockerd mode
export DOCKER_HOST=$HOME/.rd/docker.sock

act --container-architecture linux/amd64 -l
# Stage  Job ID                  Job name                Workflow name                 Workflow file          Events
# 0      ubuntu-town             ubuntu-town             GHA Handy Workflow Reference  GHA.actions-handy.yml  push,workflow_dispatch
# 0      official-actions-usage  official-actions-usage  GHA Handy Workflow Reference  GHA.actions-handy.yml  push,workflow_dispatch
# 0      just-macos-things       just-macos-things       GHA Handy Workflow Reference  GHA.actions-handy.yml  push,workflow_dispatch
# 0      on-failure              on-failure              Merge Release Branch and Tag  main.yml               workflow_run
# 0      merge-and-tag           merge-and-tag           Merge Release Branch and Tag  main.yml               workflow_run
# 0      release                 release                 Release desertislandutils     release.yml            workflow_run
# 0      poetry-run-tests        poetry-run-tests        Test desertislandutils        test.yml               push,pull_request,workflow_dispatch

act --container-architecture linux/amd64 -j poetry-run-tests -P macos-latest=-self-hosted
# dang

-P ubuntu-18.04=nektos/act-environments-ubuntu:18.04

```