import datetime as dt
import random
from datetime import datetime, timedelta

import plac


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


def check_date(filename, start_date=dt.date(2022, 7, 1), end_date=dt.date.today()):
    dates = dates_range(start_date=start_date, end_date=end_date, filename=filename)
    if dates:
        random_date = random.choice(dates).strftime('%Y-%m-%d')
        print(f'Take task from this date: {random_date}')
        return random_date
    print(f'All tasks in a period from {start_date} to {end_date} are done.')
    return


def execute_tasks_in_period():
    filename = 'processed_dates.txt'
    while True:
        date = check_date(filename)
        if date:
            answer = input('y/N')
            if answer == 'y':
                with open(filename, 'a') as file_with_dates:
                    file_with_dates.write(f"{date}\n")
        else:
            break


if __name__ == '__main__':
    plac.call(execute_tasks_in_period)
