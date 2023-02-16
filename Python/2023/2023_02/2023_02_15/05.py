import calendar
import os


# def func(self, year, month):
#     self.year = year
#     self.month = month

def yyyyDir():
    year = int(input('Enter the year: '))
    try:
        # Create Year Directory if not exists
        if not os.path.exists(year):
            os.mkdir(str(year))
            os.chdir(str(year))
            monthDir(year)

        else:
            if os.path.exists(year):
                os.chdir(year)
                monthDir(year)
    except:
        print(f'{year} Already Exists')


def monthDir(year):
    for month in range(1, 13):
        yyyy_mm = f'{year}_{str(month).zfill(2)}'
        # print(yyyy_mm)
        try:
            # Create Months Directory if not exists
            if not os.path.exists(yyyy_mm):
                os.mkdir(yyyy_mm)
                os.chdir(yyyy_mm)
                dayDirs(month, year)
            else:
                os.chdir(yyyy_mm)
                dayDirs(month, year)
        except:
            print(f'{yyyy_mm} Already Exists')


def dayDirs(month, year):
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        yyyy_mm_dd = f'{year}_{str(month).zfill(2)}_{str(day).zfill(2)}'
        print(yyyy_mm_dd)
        # Create Dates Directory if not exists
        if not os.path.exists(yyyy_mm_dd):
            os.mkdir(yyyy_mm_dd)


# print(calendar.monthrange(year, 2)[1])
#
# print(type(calendar.monthrange(year, 2)[1]))



# try:
#     # Create Months Directory if not exists
#     if not os.path.exists(yyyy_mm):
#         os.mkdir(yyyy_mm)
#         os.chdir(yyyy_mm)
#         dayDirs(month, year)
#     else:
#         os.chdir(yyyy_mm)
#         dayDirs(month, year)
# except:
#     print(f'{yyyy_mm} Already Exists')
