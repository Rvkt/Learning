import os
from datetime import date, datetime


now = datetime.now()
year_full = now.strftime('%Y')
year_short = now.strftime('%y').zfill(2)
month_str = now.strftime('%b').upper()
month_int = now.strftime('%m').zfill(2)
day_month = now.strftime('%d').zfill(2)
day_year = now.strftime('%j').zfill(2)
hour_24 = now.strftime('%H').zfill(2)
hour_12 = now.strftime('%I').zfill(2)
minutes = now.strftime('%M').zfill(2)
amPm = now.strftime('%p').upper()


try:
    if not os.path.exists(year_full):
        os.mkdir(year_full)
    else:
        print(f'{year_full} already exists !!')
except:
    pass

os.chdir(year_full)


dict = {

# 'yr':               f'{year_full}',
'ym1':              f'{year_full}{month_str}',
'ymd1':             f'{year_full}{month_str}{day_month}',
'ymdhm1':           f'{year_full}{month_str}{day_month}{hour_24}{minutes}',

'ym2':              f'{year_full}{month_int}',
'ymd2':             f'{year_full}{month_int}{day_month}',
'ymdhm4':           f'{year_full}{month_int}{day_month}{hour_24}{minutes}',

'ym3':              f'{year_short}{month_str}',
'ymd3':             f'{year_short}{month_str}{day_month}',
'ymdhm7':           f'{year_short}{month_str}{day_month}{hour_24}{minutes}',

'ymd4':             f'{year_short}{month_int}{day_month}',
'ymdhm10':          f'{year_short}{month_int}{day_month}{hour_24}{minutes}',

}


print('\t-----------> Directory name starts with Year:')
for value in dict.values():
    print(value)
    try:
        if not os.path.exists(value):
            os.mkdir(value)
        else:
            print(f'{value} already exists !!')
    except:
        pass