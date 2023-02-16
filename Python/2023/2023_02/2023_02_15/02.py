import calendar
import os

year = 2023


def numDays():
    for i in range(1, 13):
        # print(f'Number of days in {str(i).zfill(2)} = {calendar.monthrange(year, i)[1]}')
        for day in range(1, calendar.monthrange(year, i)[1] + 1):
            # print(f'{year}_{str(i).zfill(2)}_{str(day).zfill(2)}')
            os.mkdir(f'{year}_{str(i).zfill(2)}_{str(day).zfill(2)}')


def monthDir():
    for month in range(1, 13):
        print(str(month).zfill(2))
        os.mkdir(f'{year}_{str(month).zfill(2)}')


def yearDir():
    try:
        if not os.path.exists(year):
            os.mkdir(str(year))
            os.chdir(str(year))
            print(os.getcwd())
            # monthDir()
            numDays()
    except:
        os.chdir(str(year))
        print(os.getcwd())
        # monthDir()
        numDays()



yearDir()

