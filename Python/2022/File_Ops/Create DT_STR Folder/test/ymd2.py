from datetime import date, datetime
from calendar import monthrange
import os

date = date.today()
now = datetime.now()
year = now.strftime('%Y')
month_int = now.strftime('%m')
# print(month_int)
yearmonth = now.strftime('%Y%m')
# print(yearmonth)
daysInMonth= monthrange(date.year, date.month)[1]

dayNum = []
for i in range((daysInMonth)):
    dayNum.append(f'{year}{month_int}{str(i+1).zfill(2)}')
# print(f'{dayNum}')

'''
for i in dayNum:
    print(i)
    '''
    
'''
try:
    if not os.path.exists(year):
        os.mkdir(year)
        print(f'{year} is created!')
    else:
        
        if os.path.exists(year):
            os.chdir(year)
            print(f'Directory change to {year}!')
            # print(os.getcwd())
            if not os.path.exists(yearmonth):
                os.mkdir(yearmonth)
                print(f'{yearmonth} is created!')
            else:
                if os.path.exists(yearmonth):
                    os.chdir(yearmonth)
                    print(f'Directory change to {yearmonth}!')
                    print(os.getcwd())
except:
    pass
'''

for f in os.listdir(os.getcwd()):
    if not os.path.exists(year):
        os.mkdir(year)
    else:
        os.chdir(year)
        print(os.getcwd())
        for f in os.listdir(os.getcwd()):
            if not os.path.exists(yearmonth):
                os.mkdir(yearmonth)
            else:
                os.chdir(yearmonth)
                print(os.getcwd())