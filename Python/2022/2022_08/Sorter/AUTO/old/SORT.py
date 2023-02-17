# Create folder with name as current year, month and date in the given directory.
# Create sub-folders.

import os
import shutil
from datetime import date

today = date.today()
year = today.strftime('%Y')
month = today.strftime('%b').upper()
day = today.strftime('%d')


dt_path = f'{year}{month}{day}'
dstn = input('Enter Path:\n')
files = os.listdir(dstn)
# os.chdir(dstn)


# Create folder with name as current year, month and date.
# os.mkdir(dt_path)
# os.chdir(dt_path)



# for f_name in files:
#     if f_name[0] != '.':
#         f_ext = f_name.split('.')[-1]
#         print(f_ext)


# for file in files:
#     filename, extension = os.path.splitext(file)
    # extension = extension[1:]
        # print(extension)
    # for sub_folder in [extension]:
    #     os.mkdir(sub_folder)
