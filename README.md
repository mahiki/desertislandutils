# desertislandutils
[![PyPI version](https://badge.fury.io/py/desertislandutils.svg)](https://pypi.org/project/desertislandutils/)

A collection of personal convenience utilities for managing parallel directory structures and ISO week numbers. Written in Python because it's far better than shell scripting!

## Installation

Install globally using `uv`:

```sh
uv tool install desertislandutils
```

Update to the latest version:

```sh
uv tool upgrade desertislandutils
```

## The Utils

### toobigdatadoc (`too`)

Manage parallel directory structures for separating text files from large binary files and datasets. Creates symlinked folders under `HOME/{toobig|toodata|toodoc}`:

- `toobig` - Large files excluded from backups
- `toodata` - Small-ish data files  
- `toodoc` - Binary files like PDFs and images

```
$HOME
    |-- toobig
        |-- # replicated folder paths with large files here, assume not to be backed up
    |-- toodata
        |-- # small-ish data files in support of the parallel root
    |-- toodoc
        |-- # usually pdfs or image files
```

**Usage:**

```sh
too --help

usage: too [-h] {big,data,doc}

Create symlinked parallel folders under HOME/{toobig|toodata|toodoc}, to
contain data/binary files outside of git repo or away from source/text files.

positional arguments:
  {big,data,doc}  large files to exclude from backup, smallish datasets,
                  binary files like pdf

options:
  -h, --help      show this help message and exit
```

### weeknumber (`wn`)

Get ISO year week numbers in YYYY-WDD format. Default weekend day is Saturday.

**Usage:**

```sh
wn --help

 Usage: wn [OPTIONS] [DATE]                                                     
                                                                                
 ISO year week number of a date as YYYY-"W"WW. Default weekend day is Saturday.
                                                                                
 Example:                                                                       
                                                                                
 $> wn 'Jul 22 2020' --last                                                     
                                                                                
 2020-W29                                                                       
                                                                                
╭─ Arguments ────────────────────────────────────────────────────────────────╮
│   date      [DATE]  A text expression of date, ex: 'November 27', or      │
│                     2112-07-29. Default is todayʼs in current TZ.          │
│                     [default: (dynamic)]                                   │
╰────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────╮
│ --sunday              Week end is Saturday by default, this flag sets     │
│                       Sunday weekend day (ISO standard).                   │
│ --last                Give week number of most recently completed week    │
│                       (overrides DATE argument).                           │
│ --verbose      -v     Full parsed date details for verification.          │
│ --install-completion  Install completion for the current shell.           │
│ --show-completion     Show completion for the current shell, to copy it   │
│                       or customize the installation.                       │
│ --help                Show this message and exit.                          │
╰────────────────────────────────────────────────────────────────────────────╯
```

**Examples:**

```sh
# Get current week number
wn

# Get week number for a specific date
wn 'Jul 22'

# Get last completed week number
wn --last

# Parse a specific date with details
wn 'November 27 2024' --verbose
```

---

## Development

Built with modern Python tooling:

- **Build system:** `uv`
- **Deploy:** PyPI via GitHub Actions CI/CD
- **Package manager:** `uv`

### Setup

```sh
# Clone the repository
git clone https://github.com/mahiki/desertislandutils.git
cd desertislandutils

# Install dependencies (including dev extras)
uv sync --all-extras
```

### Testing

```sh
# Run tests
just test

# Or directly with uv
uv run --extra test pytest --disable-warnings --verbose
```

### Local Development

```sh
# Run commands directly from source
uv run wn --help
uv run too --help
```

### Project Tasks

See the `justfile` for available commands:

```sh
just --list
```

## License

MIT