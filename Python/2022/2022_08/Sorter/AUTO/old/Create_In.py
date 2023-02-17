# Create folder with name as current year, month and date in the current directory.
# Create sub-folders.

import os
from datetime import date

today = date.today()
year = today.strftime('%Y')
month1 = today.strftime('%m').upper()
month2 = today.strftime('%b').upper()
day = today.strftime('%d')


dir_path1 = f'{year}{month1}{day}'
# Output --> YYYYMMDD
dir_path2 = f'{year}{month2}{day}'
# Output --> YYYYMMMDD


# Create folder with name as current year, month and date.
os.mkdir(dir_path1)
os.mkdir(dir_path2)



# os.chdir(dir_path1)
# for sub_folder in ['01', '02', '03', '04']:
#     # Create sub-folders.
#     os.mkdir(sub_folder)
