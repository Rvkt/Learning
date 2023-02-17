# Create folder with name as current year, month and date in the given directory.
# Create sub-folders.

import os
from datetime import date

today = date.today()
year = today.strftime('%Y')
month = today.strftime('%m').upper()
day = today.strftime('%d')


dir_path = f'{year}{month}{day}'
dstn = input('Enter Path:\n')
os.chdir(dstn)


# Create folder with name as current year, month and date.
os.mkdir(dir_path)
os.chdir(dir_path)
for sub_folder in ['01', '02', '03', '04']:
    # Create sub-folders.
    os.mkdir(sub_folder)
