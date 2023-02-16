import calendar
import os


def yearDir():
    year = int(input('Enter the year: '))
    try:
        # Create Year Directory if not exists
        if not os.path.exists(year):
            os.mkdir(str(year))
            os.chdir(str(year))
            monthDir(year)


    except:
        print(f'{year} Already Exists')


def monthDir(year):
    month_count = 0
    while month_count < 13:
        for month in range(1, 13):
            yyyy_mm = f'{year}_{str(month).zfill(2)}'
            # print(yyyy_mm)
            if not os.path.exists(yyyy_mm):
                os.mkdir(yyyy_mm)
                os.chdir(yyyy_mm)
                daysDirs(year, month)

        month_count += 1


def daysDirs(year, month):
    day_count = 0

    while day_count < calendar.monthrange(year, month)[1] + 1:
        if day_count == calendar.monthrange(year, month)[1]:
            os.chdir(year)
            yearDir()

        for day in range(1, calendar.monthrange(year, month)[1] + 1):
            yyyy_mm_dd = f'{year}_{str(month).zfill(2)}_{str(day).zfill(2)}'
            # print(yyyy_mm_dd)
            os.mkdir(yyyy_mm_dd)

        day_count += 1


yearDir()