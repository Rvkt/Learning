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

day_dict = {'dhm': f'{day_month}{hour_24}{minutes}'}

for value in day_dict.values():
    print(f'\n\tDirectory Name: {value}')
    try:
        if not os.path.exists(value):
            os.mkdir(value)
        else:
            print(f'\t{value} already exists !!')
    except:
        pass