# Create dir and sub dirs
import os
from datetime import date

path = input('Enter Destination Path: ')
os.chdir(path)
dstn = input('Enter Folder Name: ')
year = input ('Enter Year: ')
dir_name = f'{dstn}_{year}'
# print(os.getcwd())
os.mkdir(dir_name)
os.chdir(dir_name)
# print(os.getcwd())

month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

for m in month:
    os.mkdir(f'{year}_{m}')
    print(f'{year}_{m} is created in {dir_name}')