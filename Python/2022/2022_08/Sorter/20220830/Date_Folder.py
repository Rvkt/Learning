import os
from datetime import date, datetime

now = datetime.now()
dt_int = now.strftime('%Y%m%d')
dt_str = now.strftime('%Y%b%d')

if not os.path.exists(dt_int):
    os.mkdir(dt_int)
else:
    print('Already Exits')

if not os.path.exists(dt_str.upper()):
    os.mkdir(dt_str.upper())
else:
    print('Already Exits')