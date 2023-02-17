import os
import shutil
# from datetime import date

path = input('Enter Path: ')
files = os.listdir(path)

# today = date.today()
# os.makedirs(today.strftime('%Y%b%d').upper())

for file in files:
    name, ext = os.path.splitext(file)
    ext = ext[1:]
    
    if ext == '':
        continue

    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)