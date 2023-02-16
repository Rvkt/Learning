import calendar
import os

year = 2023


for month in range(1, 13):
    yyyy_mm = f'{year}_{str(month).zfill(2)}'
    print(yyyy_mm)
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        if day == calendar.monthrange(year, month)[1] + 1:
            print(day)
            break
        else:
            yyyy_mm_dd = f'{year}_{str(month).zfill(2)}_{str(day).zfill(2)}'
            print(yyyy_mm_dd)



            # print(f'\n{yyyy_mm} Month Starts \n')

            # day = 1
            # result = 1
            #
            # while result != 0 and day < calendar.monthrange(year, month)[1] + 1:
            #     yyyy_mm_dd = f'{year}_{str(month).zfill(2)}_{str(day).zfill(2)}'
            #     day += 1
            #
            #     print(yyyy_mm_dd)

            # for day in range(1, calendar.monthrange(year, month)[1] + 1):
            #     if day == calendar.monthrange(year, month)[1] + 1:
            #         print('next month')
            #         break
            #     yyyy_mm_dd = f'{year}_{str(month).zfill(2)}_{str(day).zfill(2)}'
            #     print(yyyy_mm_dd)



# print(calendar.monthrange(year, 2)[1])
