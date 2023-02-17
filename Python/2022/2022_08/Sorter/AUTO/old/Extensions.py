import os
from pathlib import Path

dstn = input('Enter Path:\n')
files = os.listdir(dstn)

os.chdir(dstn)

fnm = []
f_ext=[]

for file in files:
    f = Path(file)
    name, ext = f.stem, f.suffix
    ext = ext[1:]
    fnm.append(name)
    # f_ext.append(ext)
    print(ext)

no_dupes_filename = [x for n, x in enumerate(fnm) if x not in fnm[:n]]
# no_dupes_ext = [x for n, x in enumerate(ext) if x not in ext[:n]]



# print(fnm)







# for file in files:
#     filename, extension = os.path.splitext(file)
#     extension = extension[1:]
#     print(extension)


