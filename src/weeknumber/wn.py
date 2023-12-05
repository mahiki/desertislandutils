"""
CLI utility that gives the ISO reporting week for a given date. 
Option allows week ending day of Saturday or Sunday.
Option for week number of most recently completed week.
Example: wn --last
    2023-W48
"""
# TODO: wont need to quote DATE if arguments are List type, and " ".join()

import os
import pendulum
import typer
from typing_extensions import Annotated, Optional, List

app = typer.Typer()

def input_date_validate(value: str):
    try:
        pendulum.parse(value, strict=False)
    except Exception as ex:
        raise typer.BadParameter(f"Unparseable date string: {value}, try YYYY-MM-DD format.")
        # os._exit(0)
    return value

def today_datestring():
    return pendulum.now().strftime("%Y-%m-%d")

def week_number_string(date, sunday_weekend = False):
    if sunday_weekend:
        return date.strftime("%Y-W%V")
    else:
        return date.add(days=1).strftime("%Y-W%V")

@app.command()
def main(
    date: Annotated[str
        , typer.Argument(
            callback=input_date_validate
            , help="A text expression of date, ex: 'November 27', or 2112-07-29"
            , default_factory=today_datestring)]
    , sunday_weekend: Annotated[bool
        , typer.Option(
            "--sunday"
            , help="Weekend is Saturday by default, this flag sets Sunday weekend day.")] = False
    , last_week: Annotated[bool
        , typer.Option(
            "--last"
            , help="Give week number of most recently completed week (overrides DATE argument).")] = False
    , verbose: bool = False
    ):
    """
    ISO year week number of a date as YYYY-WDD. Default weekend day is Sat.

    Example:

    $> wn 'Jul 22'

    2023-W29
    """
    parsed_date = pendulum.parse(date, strict=False)

    if verbose:
        typer.echo(f"Input date string: {date}")
        typer.echo(f"Timezone: {pendulum.now().timezone.name}")
        typer.echo(f"Parsed date: {parsed_date.strftime('%Y-%m-%d')}")
        typer.echo("ISO week number:")

    if last_week:
        result = week_number_string(parsed_date.subtract(weeks=1), sunday_weekend=sunday_weekend)
    else:
        result = week_number_string(parsed_date, sunday_weekend=sunday_weekend)

    typer.echo(result)