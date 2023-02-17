import os

# Specify the directory path
path = input('Enter file path: \n')
file = input('Enter file name with extension: \n')

# Creating a file at specified folder
# join directory and file path
with open(os.path.join(path, file), 'w') as fp: