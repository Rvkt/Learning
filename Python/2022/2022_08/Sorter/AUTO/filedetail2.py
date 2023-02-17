import os.path, time
import pathlib

f_name = pathlib.Path(r'.\detail.txt')



print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
print("Created: %s" % time.ctime(os.path.getctime("test.txt")))