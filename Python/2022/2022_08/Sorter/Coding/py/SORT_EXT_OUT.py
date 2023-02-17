import os
import shutil
from datetime import date

path = input('Enter Path: ')
files = os.listdir(path)

"""
    # today = date.today()
    # os.makedirs(today.strftime('%Y%b%d').upper())
"""


for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(path + '/' + extension):
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
    else:
        os.makedirs(path + '/' + extension)
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)