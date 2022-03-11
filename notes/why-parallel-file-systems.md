# WHY DO TOOBIGDATADOC?
>What is the point of parallel file system with text notes separate to image/pdf/data files?

## TOPLINE
I decide I like my personally generated notes kept separate. They are more coherent as a block, and they are far more valuable than the mixture of images and pdf docs churning all around. I will never want to see most of those, except as specific reference from my notes. The notes are the important part reflecting my thoughts.

## REVIEW
The original problem was working git repos with markdown notes and associated pdfs, images or data files that I wanted to keep in subfolders. These couldn't be pushed into gitfarm at work, there was no LFS large file storage like github.
And do you want Large File Storage remotely?

Q: What about LFS?
A: Maybe, for repo-only perhaps this is convenient. 

Q: LFS Cons?
A: Cons - have to track each file, vs. create a linked folder and dump many files in there.

**I think for repos I much prefer parallel files vs. LFS remote storage**

Q: what about keeping images, pdfs, datafiles right alongside your text notes?
A: This is the crux of it. Seems messy to me.

**I think the convenience is browseable folders, esp. quicklook**

Q: What do you like about keeping separate?
A: The `andromeda` folder becomes a complete set of notes, journal, project ideas, all in text. Very portable, very useable for the long term. You don't need this in source control, but its nicely small. Accessing the data/doc resources isn't a big deal if needed, but those are not the most important thing.

**When browsing a complicated file system, the most important items are my personal notes**. These took time to write, they become hard to find mixed in with a ton of documents. I spent time thinking and writing about things, these are worthy of review, revisiting.  A bunch of printouts, datafiles, pdfs its mostly random shit.  My thoughts are more coherent taken all together.

## LOOK AT COMBINED ALTERNATIVE
```bash
## PARALLEL STORAGE EXAMPLE ##
Tree $HOME/toodoc -L 4
/Users/segovia/toodoc
    ├── andromeda
    │   └── school-search
    │       └── spruce-street
    ├── iterm-colors
    └── journal-in-markdown
        └── personal-journal
            └── 2021
                ├── 2021-04-08_alexey-researcher-chat.png
                ├── 2021-12-21_aaron-50th-birthday-chat_001.png
                ├── 2021-12-21_aaron-50th-birthday-chat_002.png
                └── 2021-12-21_aaron-50th-birthday-chat_003.png

tree /Users/segovia/andromeda/ -L 4
/Users/segovia/andromeda
    ├──journal-in-markdown
        ├── journal
            └── 2021
                ├── 2021-12-10_Aaron-call-on-50th.md
                ├── 2021-12-25.christmastime-is-here.md
                ├── 2022-07-09_house-help-poll.md
                ├── 2022-03-10.another-example.md
                └── doc ->  ../../../../../toodoc/andromeda/journal-in-markdown/personal-journal/2021/doc
                # or absolute one:
                └── doc ->  /Users/segovia/toodoc/andromeda/journal-in-markdown/personal-journal/2021/doc


## MIXED STORAGE EXAMPLE ##
tree /Users/segovia/andromeda/ -L 4
/Users/segovia/andromeda
    ├──journal-in-markdown
        ├── journal
            └── 2021
                ├── 2021-12-10_Aaron-call-on-50th.md
                ├── 2021-12-25.christmastime-is-here.md
                ├── 2022-07-09_house-help-poll.md
                ├── 2022-03-10.another-example.md
                ├── 2021-04-08_alexey-researcher-chat.png
                ├── 2021-12-21_aaron-50th-birthday-chat_001.png
                ├── 2021-12-21_aaron-50th-birthday-chat_002.png
                └── 2021-12-21_aaron-50th-birthday-chat_003.png
```
