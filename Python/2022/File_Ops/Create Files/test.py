import os

# Specify the directory path
path = input('Enter file path: \n')
#file = input('Enter file name with extension: \n')

file_list = ['index.html', 'style.css', 'script.js']

# Creating a file at specified folder
# join directory and file path

for file in file_list:
    with open(os.path.join(path, file), 'w'):
    print(f'{file} is created')