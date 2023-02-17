import os
from datetime import *

now = datetime.now()
dt_str = now.strftime('%Y%m%d')

if not os.path.exists(dt_str):
    os.mkdir(dt_str)
else:
    print('Already Exits')
