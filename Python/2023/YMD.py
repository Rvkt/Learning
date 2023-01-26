from datetime import datetime
import os

now = datetime.now()
year = int(now.strftime('%Y'))
month_int = (now.strftime('%m').zfill(2))
day = now.strftime('%d')
date_str = f'{year}{month_int}{day}'
print(date_str)

os.mkdir('today')

os.mkdir(date_str)
