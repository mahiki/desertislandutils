# Build on Github
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
