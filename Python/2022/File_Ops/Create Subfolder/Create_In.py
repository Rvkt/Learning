# Create folder with name as current year, month and date in the current directory.
# Create sub-folders.

import os
from datetime import date

today = date.today()
year = today.strftime('%Y')
month = today.strftime('%b').upper()
day = today.strftime('%d')

dt_str = f'{year}{month}{day}'
# path = 'c:/Users/Dabba/Desktop/automation/Test'

# Create folder with name as current year, month and date.
os.mkdir(dt_str)
os.chdir(dt_str)
for sub_folder in ['01', '02', '03', '04']:
    # Create sub-folders.
    os.mkdir(sub_folder)
