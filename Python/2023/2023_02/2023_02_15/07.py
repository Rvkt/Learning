import calendar
import os


def yearDir():
    year = int(input('Enter the year: '))
    try:
        # Create Year Directory if not exists
        if not os.path.exists(year):
            os.mkdir(str(year))
            # Change directory to Year Directory
            os.chdir(str(year))
            print(os.getcwd())
            # Call monthDir Function
            monthDir(year)


    except:
        print(f'{year} Already Exists')


def monthDir(year):
    # os.chdir(str(year))
    for month in range(1, 13):
        yyyy_mm = f'{year}_{str(month).zfill(2)}'

        if not os.path.exists(yyyy_mm):
            os.mkdir(yyyy_mm)
            os.chdir(yyyy_mm)
            print(os.getcwd())
            # Call dayDir Function
            dayDir(month, year)


def dayDir(month, year):
    os.mkdir(f'{year}_{month}_Test')
    os.chdir(year)
    print(os.getcwd())
    monthDir(year)


yearDir()
