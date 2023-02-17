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


dict = {

'yr':               f'{year_full}',
'ym1':              f'{year_full}{month_str}',
'ymd1':             f'{year_full}{month_str}{day_month}',
'ymdhm1':           f'{year_full}{month_str}{day_month}{hour_24}{minutes}',
'ymdhm2':           f'{year_full}{month_str}{day_month}{hour_12}{minutes}',
'ymdhm3':           f'{year_full}{month_str}{day_month}{hour_12}{minutes}{amPm}',

'ym2':              f'{year_full}{month_int}',
'ymd2':             f'{year_full}{month_int}{day_month}',
'ymdhm4':           f'{year_full}{month_int}{day_month}{hour_24}{minutes}',
'ymdhm5':           f'{year_full}{month_int}{day_month}{hour_12}{minutes}',
'ymdhm6':           f'{year_full}{month_int}{day_month}{hour_12}{minutes}{amPm}',

'ym3':              f'{year_short}{month_str}',
'ymd3':             f'{year_short}{month_str}{day_month}',
'ymdhm7':           f'{year_short}{month_str}{day_month}{hour_24}{minutes}',
'ymdhm8':           f'{year_short}{month_str}{day_month}{hour_12}{minutes}',
'ymdhm9':           f'{year_short}{month_str}{day_month}{hour_12}{minutes}{amPm}',

'ymd4':             f'{year_short}{month_int}{day_month}',
'ymdhm10':          f'{year_short}{month_int}{day_month}{hour_24}{minutes}',
'ymdhm11':          f'{year_short}{month_int}{day_month}{hour_12}{minutes}',
'ymdhm12':          f'{year_short}{month_int}{day_month}{hour_12}{minutes}{amPm}'

}

month_dict = {

'month':            f'{month_str}',
'month2':           f'{month_int}',

'md':               f'{month_str}{day_month}',
'md2':              f'{month_int}{day_month}',

'mdhm':             f'{month_str}{day_month}{hour_24}{minutes}',
'mdhm2':            f'{month_str}{day_month}{hour_12}{minutes}',
'mdhm3':            f'{month_str}{day_month}{hour_12}{minutes}{amPm}',

'mdhm4':            f'{month_int}{day_month}{hour_24}{minutes}',
'mdhm5':            f'{month_int}{day_month}{hour_12}{minutes}',
'mdhm6':            f'{month_int}{day_month}{hour_12}{minutes}{amPm}',


}

print('\t-----------> Starts with Year:')
for value in dict.values():
    print(value)

print('\t-----------> Starts with Year:')

