year = int(now.strftime('%Y'))
import os

def leap_yr():
    if (year % 400 == 0) and (year % 100 == 0):
        print("{0} is a leap year, FEB28 Exists !!".format(year))

    elif (year % 4 == 0) and (year % 100 != 0):
        print("{0} is a leap year, FEB28 Exists !!".format(year))

    else:
        print("{0} is not a leap year, FEB28 Not Exists !!".format(year))

leap_yr()