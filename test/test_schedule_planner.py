import sys

sys.path.insert(0, 'src')

from src.schedule_planner import dates_range
import datetime as dt

YEAR = 2023
MONTH_JULY = 7


def test_dates_range_with_empty_file():
    assert dates_range(
        start_date=dt.date(year=YEAR, month=MONTH_JULY, day=1),
        end_date=dt.date(year=YEAR, month=MONTH_JULY, day=3),
        filename='test/resources/file_with_no_dates.txt'
    ) == [
               dt.date(YEAR, MONTH_JULY, 1),
               dt.date(YEAR, MONTH_JULY, 2),
               dt.date(YEAR, MONTH_JULY, 3)
           ]


def test_dates_range_with_non_empty_file():
    assert dates_range(
        start_date=dt.date(year=YEAR, month=MONTH_JULY, day=1),
        end_date=dt.date(year=YEAR, month=MONTH_JULY, day=3),
        filename='test/resources/file_with_dates.txt'
    ) == [
               dt.date(YEAR, MONTH_JULY, 2),
               dt.date(YEAR, MONTH_JULY, 3)
           ]
