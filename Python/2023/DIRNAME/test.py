from datetime import date, datetime
from calendar import monthrange
import os


path = os.getcwd()
os.chdir(path)

now = datetime.now()
year = now.strftime('%Y')

if not os.path.exists(year):
    os.mkdir(year)
    

month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']


dirName = []


for m in iter(month):
    # print(f"No. of Days of {str(m).zfill(2)}: {monthrange(int(year), int(m))[1]}")
    if not os.path.exists(f'{year}{str(m).zfill(2)}'):
        os.mkdir(f'{year}{str(m).zfill(2)}')

    daysRange = monthrange(int(year), int(m))[1]
    for d in range(1, daysRange+1):
        print(f'{year}{str(m).zfill(2)}{str(d).zfill(2)}')
        dirName.append(f'{year}{str(m).zfill(2)}{str(d).zfill(2)}')
        

#for a in dirName:
#    if not os.path.exists(a):
#        os.mkdir(a)