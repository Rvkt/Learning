# Create Current Date Folder In the Given Path
import os
from pathlib import *
import errno
from datetime import *

today = date.today()
year = today.strftime('%Y')
month = today.strftime('%b').upper()
day = today.strftime('%d')

# dir_path = f'{year}{month}{day}'

dt_str = Path(f'{year}{month}{day}')
path = input('Enter Path: ')

os.chdir(path)

try:
    os.mkdir(dt_str)
except OSError as e:
    if e.errno == errno.EXIST:
        pass


# sourcepath = os.getcwd()

# print(os.getcwd())
