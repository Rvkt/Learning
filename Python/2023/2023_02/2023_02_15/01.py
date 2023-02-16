import calendar, os
from calendar import monthcalendar
from datetime import datetime

now = datetime.now()

# year = now.strftime('%Y')
month_int = (now.strftime('%m').zfill(2))
numDays1 = calendar.monthrange(now.year, now.month)[1]

# print(numDays1)

year = 2023


def yearDir():
    try:
        if not os.path.exists(year):
            os.mkdir(str(year))
            os.chdir(str(year))
            print(os.getcwd())
    except:
        os.chdir(str(year))
        print(os.getcwd())


def monthDays():
    for month in range(1, 13):
        yyyy_mm = f'{year}_{str(month).zfill(2)}'
        print(yyyy_mm)
        for day in range(1, calendar.monthrange(year, month)[1] + 1):
            yyyy_mm_dd = f'{year}_{str(month).zfill(2)}_{str(day).zfill(2)}'
            print(yyyy_mm_dd)



# print(monthcalendar(2023, 2))

# Give the Calendar of the year
# print(calendar.calendar(2023))
