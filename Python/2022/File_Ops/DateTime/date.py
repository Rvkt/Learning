import calendar, os
from datetime import date, datetime

now = datetime.now()
yr = now.strftime('%Y')
day = now.strftime('%d').zfill(2)
month = calendar.month_abbr[1:]
print(month)
yymm = []

for dir in os.getcwd():
    if not os.path.exists(yr):
        os.mkdir(yr)
    else:
        for i in month:
            yymm.append(f'{yr}{i.upper()}')
            print(yymm)

for i in yymm:
    os.chdir(yr)
    try:
        os.mkdir(i)
    except:
        print(f"{i} Already Exists!!")
  