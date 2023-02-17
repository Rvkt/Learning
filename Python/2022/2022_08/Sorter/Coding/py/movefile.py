import os
import shutil


srcpath = input('Enter path: ')
dstnpath = input('Enter path: ')

srcpath = 'C:/Users/Dabba/Desktop/automation/src'
srcfiles = os.listdir(srcpath)
dstnpath = 'C:/Users/Dabba/Desktop/automation/dstn'
for file in srcfiles:
    if file.endswith('.txt'):
        shutil.move(os.path.join(srcpath, file), os.path.join(dstnpath, file))



