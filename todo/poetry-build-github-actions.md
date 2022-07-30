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


example marketplace actions that might help:

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

## TODO: bump version numbers
I guess a git hook that runs `./bump_version.sh` when pulling a release branch?

----------
## EMPATHY
[example: gha poetry]: https://github.com/marketplace/actions/python-poetry-action

[example2: gha poetry]: https://github.com/ppeetteerrs/simple-poetry

[semantic release]: https://mestrak.com/blog/semantic-release-with-python-poetry-github-actions-20nn

[GHA desertislandutils publish python package on release]: https://github.com/mahiki/desertislandutils/actions/new?category=none&query=python
