# PROBLEM with Poetry and Pytest: passing arguments in main
* adding main(toodir) argument works as a script, `poetry run python too.py`
* fails as a cli with `poetry run too -h`, missing positional argument
* need to call `main(args)` in pytest scripts

but poetry does this to make the executable:
```sh
rich /Users/segovia/Library/Caches/pypoetry/virtualenvs/desertislandutils-AVSNhiuH-py3.9/bin/too
#!/Users/segovia/Library/Caches/pypoetry/virtualenvs/desertislandutils-AVSNhiuH-py3.9/bin/python
from src.toobigdatadoc.too import main

if __name__ == '__main__':
    main()
```


so poetry creates a python script called `too` that calls main with no arguments.

**How does pytest call the `too` function from poetry, with our command line arguments?**

## TOPLINE SOLUTION
The executable, poetry execution, poetry shell, or the script exection call main with no arguments, and `argparse` consumes the CLI arguments. In PyTest, we import the module and call `main(["command", "line", "arguments"])`.

Our implementation must handle both entrypoints:
1. `main()` no args + command line args
2. `main(` with function arguments from pytest

## THIS BLOG SOLVES THE PROBLEM
Jonathan Bowman
https://dev.to/bowmanjd/build-and-test-a-command-line-interface-with-poetry-python-s-argparse-and-pytest-4gab

The argument parsing function becomes the poetry script entrypoint, **NOT MAIN!!**

```toml
<!-- pyproject.toml -->
[tool.poetry.scripts]
greet = "greet.greet:cli"
```

```sh
poetry run greet -r 2 -i 1 Asia/Damascus
```

his cli function calls the parser
```py
# src/greet/greet.py
def cli(args=None):
    if not args:
        args = sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument("tz", help="The timezone")
    parser.add_argument(
        "-r",
        "--repeat",
        help="number of times to repeat the greeting",
        default=1,
        type=int,
    )
    parser.add_argument(
        "-i",
        "--interval",
        help="time in seconds between iterations",
        default=3,
        type=int,
    )
    args = parser.parse_args(args)
    greet(args.tz, args.repeat, args.interval)
```

### Testing argparse interfaces with pytest
Key passage:
>Other than accepting and testing for the existence of args, the key difference here is that ***we pass args to parse_args***(). In other words the parse_args() function will use an argument list if specified (it uses sys.argv if not)

## RSRC
[Bowmans main solution](https://dev.to/bowmanjd/build-and-test-a-command-line-interface-with-poetry-python-s-argparse-and-pytest-4gab)

[Shuklin provides simpler system exit handling](https://medium.com/python-pandemonium/testing-sys-exit-with-pytest-10c6e5f7726f)

https://stackoverflow.com/questions/67476156/pass-commandline-arguments-to-a-python-script-installed-with-poetry

https://stackoverflow.com/questions/28440441/importing-a-python-script-from-another-script-and-running-it-with-arguments

https://stackoverflow.com/questions/44283780/importing-a-python-script-module-that-uses-argparse-into-another-python-script/44630021#44630021
