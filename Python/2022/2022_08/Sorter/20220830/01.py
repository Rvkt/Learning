import os,shutil

path = (os.getcwd())
file_list = os.listdir(path)
# Print the files in the destination folder
for file in file_list:
    print(f"\tFiles in the destination folder:\n\t{file}")