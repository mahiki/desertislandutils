"""
CLI utility that gives the ISO reporting week for a given date. 
Option allows week ending day of Saturday or Sunday.
Option for week number of most recently completed week.
Example: wn --last
    2023-W48
"""

import pendulum
from pendulum.parsing.exceptions import ParserError
import typer
from typing_extensions import Annotated, Optional, List

app = typer.Typer()

def input_date_validate(value: str):
    try:
        pendulum.parse(value, strict=False)
    except ParserError as ex:
        raise typer.BadParameter(f"{ex}, try YYYY-MM-DD format.")
    return value

def today_datestring():
    return pendulum.now().to_date_string()

def week_number_string(date, sunday_weekend = False):
    if sunday_weekend:
        return date.strftime("%G-W%V")
    else:
        return date.add(days=1).strftime("%G-W%V")

def verbose_output(date, parsed_date, sunday_weekend, last_week):
    weekend_day = "Sunday" if sunday_weekend else "Saturday"

    if sunday_weekend:
        weekend_date = parsed_date.add(days=-1).next(pendulum.SUNDAY)
    else:
        weekend_date = parsed_date.add(days=-1).next(pendulum.SATURDAY)

    if last_week: weekend_date = weekend_date.subtract(weeks=1)

    typer.echo(f"Input date string: {date}")
    typer.echo(f"Timezone:          {pendulum.now().timezone.name}")
    typer.echo(f"Parsed date:       {parsed_date.to_date_string()}")
    typer.echo(f"Last week flag:    {last_week}")
    typer.echo(f"Week end day:      {weekend_day}")
    typer.echo(f"Week end date:     {weekend_date.to_date_string()}")


@app.command()
def main(
    date: Annotated[str
        , typer.Argument(
            callback=input_date_validate
            , help="A text expression of date, ex: 'November 27', or 2112-07-29. Default is today's in current TZ."
            , default_factory=today_datestring)]
    , sunday_weekend: Annotated[bool
        , typer.Option(
            "--sunday"
            , help="Week end is Saturday by default, this flag sets Sunday weekend day (ISO standard).")] = False
    , last_week: Annotated[bool
        , typer.Option(
            "--last"
            , help="Give week number of most recently completed week (overrides DATE argument).")] = False
    , verbose: bool = False
    ):
    """
    ISO year week number of a date as YYYY-"W"WW. Default weekend day is Saturday.\n
    Example:\n
    $> wn 'Jul 22 2020' --last\n
    2020-W29
    """
    parsed_date = pendulum.parse(date, strict=False)
    if verbose: verbose_output(date, parsed_date, sunday_weekend, last_week)
    
    if last_week:
        result = week_number_string(parsed_date.subtract(weeks=1), sunday_weekend=sunday_weekend)
    else:
        result = week_number_string(parsed_date, sunday_weekend=sunday_weekend)

    typer.echo(result)