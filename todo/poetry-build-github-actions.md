# Build on Github

## TODO: UNICORN-DREAM: BUILD & RELEASE
DONE: GHA `poetry run pytest`

TODO: Merge release/vX.X.X to main
TODO: Tag
TODO: Build release artifact `poetry build --format sdist`
TODO: Create release from tagged version and built thing
TODO: Get SHA from github archive URL
TODO: Call the homebrew-tap to bump formula, or just a cron to gather the update.

TODO: how to bump version numbers automatically


### Auto merge after tests
Q: how to get the name of release branch

    github.event.workflow_run...
    github.ref_name		            # The branch or tag name that triggered the workflow run.


Actually, this is much simpler. Just trigger on successful workflow:

1. checkout full repo
```sh
git checkout main
git merge --no-ff ${{github.ref_name}}
git tag -a v1.2
```

https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#running-a-workflow-based-on-the-conclusion-of-another-workflow

#### Push a commit using the built-in token
[from github actions/checkout@v3](https://github.com/marketplace/actions/checkout#Push-a-commit-using-the-built-in-token)

```yaml

on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
w      - uses: actions/checkout@v3
      - run: |
          date > generated.txt
          git config user.name github-actions
          git config user.email github-actions@github.com
          git add .
          git commit -m "generated"
          git push
```

#### example marketplace actions that might help:

https://github.com/marketplace/actions/enable-pull-request-automerge
https://github.com/OSS-Docs-Tools/code-owner-self-merge



----------
TODO: automate CI build task on push to dev, merge to main.

Github actions has pypi publisher and build templates, but dont use poetry.
The CI template should install poetry, build, and publish to pypi as usual.

    merge{dev,main} -> GHA build publish -> pypi
        triggers homebrew repo build/test/publish

    alternate:
            GHA build publish -> GH artifact
        triggers homebrew repo build/test/publish

## OFF-WORLD: strategy
* copy the CI templates from the linked repo
* they just pip install poetry and run it on 'push'

That covers the build. What about triggering homebrew repo action with new release?

## TODO: semantic versioning
[see link of semver][semantic release] for automated gh releases, using poetry.

----------
## EMPATHY
[example: gha poetry]: https://github.com/marketplace/actions/python-poetry-action

[example2: gha poetry]: https://github.com/ppeetteerrs/simple-poetry

[semantic release]: https://mestrak.com/blog/semantic-release-with-python-poetry-github-actions-20nn

[GHA desertislandutils publish python package on release]: https://github.com/mahiki/desertislandutils/actions/new?category=none&query=python
