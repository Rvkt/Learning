import calendar
from datetime import datetime

now = datetime.now()
month = (now.strftime('%m').zfill(2))
# print(month)

now = datetime.now()
year = now.strftime('%Y')
month_long = []

for i in range(1, 13):
    month_long.append(calendar.month_name[i])  # month_name is an array
for i in month_long:
    print(f'{year}{i[0:3].upper()}')

now = datetime.now()
year = now.strftime('%Y')
month_short = calendar.month_abbr[1:]

for i in month_short:
    print(f'{year}{i.upper()}')

now = datetime.now()
yr = now.strftime('%Y')
month2 = calendar.month_abbr[1:]


