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

## MANUAL BUILD
```sh
# cd  ../desertislandtils
git checkout tag v0.2.1
poetry build --format sdist

# MANUALLY UPLOAD TO GITHUB RELEASE TAG v0.2.1
curl -Ls \
    https://github.com/mahiki/desertislandutils/releases/download/v0.2.1/desertislandutils-0.2.1.tar.gz \
    | shasum -a 256

# 573c103661d99ff73a3f9749f5c3343f2e8255e36a66928a7192aaabecd056ef

cd /repo/homebrew-tap
code Formula/desertislandutils.rb

# edit URL
# edit SHA

################ NOTE: YOU MAY HAVE TO REBUILD WITH brew #################################
# If your project dependencies change then the brew pr-pull workflow may be needed,
# or brew create workflow.
##########################################################################################

# now the new version should be available
brew upgrade desertislandutils