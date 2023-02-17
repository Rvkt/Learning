import sys
from pathlib import *

def exit():
    print('<----- Program Terminated ----->')
    sys.exit()

def create_file():
    file_name = input('Enter file name: ')
    file = Path(file_name)
    if file.exists():
        print('File already exists!!')
    else:
        file.touch()
        print(f'{file_name} is created !!')

while 1:
    path = input('Enter Path:\n\t')

    print(f'{path}')

    if path =='exit':
        exit()
    else:
        create_file()