from datetime import datetime, timedelta
import datetime as dt

import random


def dates_range(start_date, end_date, filename):
    ignore_dates = []
    with open(filename, 'r') as file_with_dates:
        ignore_dates += file_with_dates.readlines()
    ignore_dates = list(map(lambda x: datetime.strptime(x.strip(), '%Y-%m-%d').date(), ignore_dates))

    dates = []
    date = start_date - timedelta(1)
    while date < end_date:
        date += timedelta(1)
        if date not in ignore_dates:
            dates.append(date)
    return dates


def check_date(filename):
    dates = dates_range(start_date=dt.date(2022, 7, 1), end_date=dt.date.today(), filename=filename)
    random_date = random.choice(dates).strftime('%Y-%m-%d')
    print(f'Take task from this date: {random_date}')
    return random_date


if __name__ == '__main__':
    filename = 'processed_dates.txt'
    while True:
        date = check_date(filename)
        answer = input('y/N')
        if answer == 'y':
            with open(filename, 'a') as file_with_dates:
                file_with_dates.write(f"{date}\n")
