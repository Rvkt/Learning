from datetime import date, datetime
from calendar import monthrange
import os

date = date.today()
now = datetime.now()
year = now.strftime('%Y')
month_int = now.strftime('%m')
ym = f'{year}{month_int}'
daysInMonth= monthrange(date.year, date.month)[1]

dayNum = []
for i in range((daysInMonth)):
    dayNum.append(f'{year}{month_int}{str(i+1).zfill(2)}')
# print(f'{dayNum}')

for i in dayNum:
    print(i)
    
try:
    if not os.path.exists(year):
        os.mkdir(year)
    else:
        print(f'{os.getcwd()}')
except:
    pass