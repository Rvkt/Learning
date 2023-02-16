import calendar
import os

year = 2000


def yyyyDir():
    try:
        if not os.path.exists(year):
            os.mkdir(str(year))
            os.chdir(str(year))
            for month in range(1, 13):
                yyyy_mm = f'{year}_{str(month).zfill(2)}'
                # print(yyyy_mm)
                try:
                    if not os.path.exists(yyyy_mm):
                        os.mkdir(yyyy_mm)
                        os.chdir(yyyy_mm)

                        for day in range(1, calendar.monthrange(year, month)[1] + 1):
                            yyyy_mm_dd = f'{year}_{str(month).zfill(2)}_{str(day).zfill(2)}'
                            # print(yyyy_mm_dd)
                            if not os.path.exists(yyyy_mm_dd):
                                os.mkdir(yyyy_mm_dd)


                except:
                    pass

            os.chdir(year)
            print(os.getcwd())

    except:
        pass

yyyyDir()

# for month in range(1, 13):
#     yyyy_mm = f'{year}_{str(month).zfill(2)}'
#
#     print(f'\n{yyyy_mm} Month Starts \n')
#
#     day = 1
#     result = 1
#
#     while result != 0 and day < calendar.monthrange(year, month)[1] + 1:
#         yyyy_mm_dd = f'{year}_{str(month).zfill(2)}_{str(day).zfill(2)}'
#         day += 1
#
#         print(yyyy_mm_dd)

# for day in range(1, calendar.monthrange(year, month)[1] + 1):
#     yyyy_mm_dd = f'{year}_{str(month).zfill(2)}_{str(day).zfill(2)}'
#     print(yyyy_mm_dd)

# print(calendar.monthrange(year, 2)[1])
