import os
from pathlib import Path

#dstn = input('Enter Path: ')

dstn = os.getcwd()

path = os.chdir(dstn)

files = os.listdir()
# print(files)

for file in files:
    # name, ext = os.path.splitext(file)
    f = Path(file)
    name, ext = f.stem, f.suffix
    splitted = name.split('.')
    print(name, ext)
    #print(splitted)

    #new_name = f'{splitted[0]}{splitted[1]} {splitted[2]}{ext}'
    #print(new_name)
# rename from os
    # os.rename(file, new_name)
# rename from pathlib    
    #f.rename(new_name)