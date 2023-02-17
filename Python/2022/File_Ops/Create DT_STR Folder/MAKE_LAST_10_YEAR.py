import os
from datetime import date, datetime
now = datetime.now()
year = int(now.strftime('%Y'))
path = input('Enter Path: ')
os.chdir(path)
for y in range(year-10, year+1):
    print(y)
    if not os.path.exists(y):
        os.mkdir(str(y))
        print(f'{y} created in {path}!')