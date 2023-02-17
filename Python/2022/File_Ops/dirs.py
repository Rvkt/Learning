import os
src = os.getcwd()
files = os.listdir(src)
print(f'\t{len(files)} Folders and files:\n')
for i, char in enumerate(files):
    print(char)