import os

# Specify the directory path
path = input('Enter file path: \n')
file_name = input('Enter file name with extension: \n')

# Creating a file at specified folder
# join directory and file path

while path == 'exit':
    break
with open(os.path.join(path, file_name), 'w') as fp:
    # uncomment below line if you want to create an empty file
    fp.write('This is a new line')
 