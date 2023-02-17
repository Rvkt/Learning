from datetime import datetime
from datetime import date, datetime
from calendar import monthrange
import os

path = os.getcwd()
os.chdir(path)

now = datetime.now()
yr = now.strftime('%Y')
month = now.strftime('%m')
yymm = now.strftime(f'{yr}{month}')
date = date.today()
daysInMonth= monthrange(date.year, date.month)[1]
dayNum = []

if not os.path.exists(yr):
    os.mkdir(yr)

for file in os.listdir(path):
    if file != yr:
        pass
    else:
        if file == yr:
            # print('Exists')
            os.chdir(yr)
print(os.getcwd())

if not os.path.exists(yymm):
    os.mkdir(yymm)
    os.chdir(yymm)
    print(os.getcwd())
else:
    if os.path.exists(yymm):
      print(f'{yymm} already exists in {os.getcwd()}')
      os.chdir(yymm)
      print(os.getcwd())

for i in range((daysInMonth)):
    dayNum.append(f'{yymm}{str(i+1).zfill(2)}')

for i in dayNum:
    if not os.path.exists(i):
      os.mkdir(i)
    else:
      print(f'{i} is already exists in the {os.getcwd()}')
