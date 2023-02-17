import os
import shutil
from pathlib import Path
from datetime import date

today = date.today()
year = today.strftime('%Y')
month = today.strftime('%m').upper()
day = today.strftime('%d')


dt_path = f'{year}{month}{day}'
dstn = input('Enter Path:\n')
files = os.listdir(dstn)
os.chdir(dstn)

# Create folder with name as current year, month and date.
if not os.path.exists(dt_path):
    os.mkdir(dt_path)

os.chdir(dt_path)

# print(os.getcwd())


for file in files:
    f = Path(file)
    name, ext = f.stem, f.suffix
    ext = ext[1:]
    for subfolder in [ext]:
        if not os.path.exists(subfolder):
            os.mkdir(subfolder)
        # print(ext)

        # if os.path.exists(dt_path + '/' + ext):
        #     shutil.move(dt_path + '/' + file, dt_path + '/' + ext + '/' + file)
        # else:
        #     os.makedirs(dt_path + '/' + ext)
        #     shutil.move(dt_path + '/' + file, dt_path + '/' + ext + '/' + file)