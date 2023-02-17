import os
import shutil
from datetime import date, datetime

now = datetime.now()
dt_str = now.strftime('%Y%m%d%H%M')

if not os.path.exists(dt_str):
    os.mkdir(dt_str)
else:
    print('Already Exits')
