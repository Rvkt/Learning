import os
from datetime import *

now = datetime.now()
year = now.strftime('%y')
month = now.strftime('%b').upper()
day = now.strftime('%d').upper()
dt_str = (f'Y{year}M{month}D{day}')

if not os.path.exists(dt_str):
    os.mkdir(dt_str)
else:
    print(f'{dt_str} Already Exits!!')