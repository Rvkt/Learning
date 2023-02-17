import os

dstn = input('Enter Path:\n')

# GET A LIST OF FILE NAMES
def filename():
    files_no_ext = [".".join(f.split(".")[:-1]) for f in os.listdir(dstn) if os.path.isfile(f)]
    print(files_no_ext)