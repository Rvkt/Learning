from datetime import datetime
from datetime import date, datetime
from calendar import monthrange
import os

path = input('Enter Path: ')
os.chdir(path)

now = datetime.now()
yr = now.strftime('%Y')
yymm = now.strftime('%Y%m')
date = date.today()
daysInMonth= monthrange(date.year, date.month)[1]
dayNum = []


if not os.path.exists(yr):
    os.mkdir(yr)
else:
    if os.path.exists(yr):
      print(f'{yr} already exists in {path}')
      os.chdir(yr)
      print(os.getcwd())

if not os.path.exists(yymm):
    os.mkdir(yymm)
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