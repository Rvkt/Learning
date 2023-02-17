from datetime import datetime
from datetime import date, datetime
from calendar import monthrange
import os

path = input('Enter Path: ')
os.chdir(path)

now = datetime.now()
year = input('Enter Year: ')
month = input('Enter Month: ')
yymm = now.strftime(f'{year}{month}')
date = date.today()
daysInMonth= monthrange(int(year), int(month))[1]
dayNum = []

if not os.path.exists(year):
    os.mkdir(year)

for file in os.listdir(path):
    if file != year:
        pass
    else:
        if file == year:
            # print('Exists')
            os.chdir(year)
# print(os.getcwd())

if not os.path.exists(yymm):
    os.mkdir(yymm)
    os.chdir(yymm)
    # print(os.getcwd())
else:
    if os.path.exists(yymm):
      print(f'{yymm} already exists in {os.getcwd()}')
      os.chdir(yymm)
    #   print(os.getcwd())

for i in range((daysInMonth)):
    dayNum.append(f'{yymm}{str(i+1).zfill(2)}')

for i in dayNum:
    if not os.path.exists(i):
      os.mkdir(i)
    else:
      print(f'{i} is already exists in the {os.getcwd()}')
