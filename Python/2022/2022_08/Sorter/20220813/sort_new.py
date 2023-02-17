import os, glob

files_list = glob.glob('*')

extension_set = set()


# Collect the file extensions into the extension set above.
for file in files_list:
    extension = file.split(sep='.')
    try:
        extension_set.add(extension[1])
    except IndexError:
        continue

# print(extension_set)


# Create subfolder
def create_dir():
    for dir in extension_set:
        try:
            os.makedirs(dir)
        except FileExistsError:
            continue

# Sort the files according to the file extension
def arrange():
    for file in files_list:
        file_ext = file.split(sep='.')
        try:
            os.rename(file, file_ext[1]+'/'+file)
        except (OSError, IndexError):
            continue


create_dir()
arrange()

print('Files are sorted!!')