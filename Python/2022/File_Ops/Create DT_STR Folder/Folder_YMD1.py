import os
from pathlib import *
import errno
from datetime import *

today = date.today()
year = today.strftime('%Y')
month = today.strftime('%b').upper()
day = today.strftime('%d')

dt_str = Path(f'{year}{month}{day}')

os.chdir(os.getcwd())

try:
    os.mkdir(dt_str)
except OSError as e:
    if e.errno == errno.EEXIST:
        pass
