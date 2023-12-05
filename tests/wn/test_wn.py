import os, time
import pendulum
from src.weeknumber.wn import main

TZ = pendulum.local_timezone().name

def test_wn_options(capsys):
    out1 = "2023-W48\n"
    main("2023-11-29")
    out, _ = capsys.readouterr()
    assert out == "2023-W48\n"

    out2 = f"""Input date string: 2112-07-24
Timezone: {TZ}
Parsed date: 2112-07-24
ISO week number:
2112-W29\n"""
    main("2112-07-24", sunday_weekend=True, verbose=True)
    out, _ = capsys.readouterr()
    assert out == out2

    out3 = f"""Input date string: 2112-07-24
Timezone: {TZ}
Parsed date: 2112-07-24
ISO week number:
2112-W30\n"""
    main("2112-07-24", sunday_weekend=False, verbose=True)
    out, _ = capsys.readouterr()
    assert out == out3

    out4 = "2112-W30\n"
    main("2112-07-24")
    out, _ = capsys.readouterr()
    assert out == out4

    out5 = "2112-W29\n"
    main("2112-07-24", last_week=True)
    out, _ = capsys.readouterr()
    assert out == out5

    out6 = pendulum.now().subtract(weeks=1).strftime("%Y-W%V")
    today = pendulum.now().strftime("%Y-%m-%d")
    main(today, last_week=True)
    out, _ = capsys.readouterr()
    assert out == out6 + "\n"
