import os
import shutil
from datetime import date

src_path = input('Enter Path: ')
files = os.listdir(src_path)


today = date.today()
year = today.strftime('%Y')
month = today.strftime('%b').upper()
day = today.strftime('%d')
# print(f'{year}{month}{day}')
dstn_path = f'{year}{month}{day}'

if not os.path.exists(dstn_path):
    os.mkdir(dstn_path)
else:
    print('Already Exits')


for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]
    
    if os.path.exists(path + '/' + extension):
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
    else:
        os.makedirs(path + '/' + extension)
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
