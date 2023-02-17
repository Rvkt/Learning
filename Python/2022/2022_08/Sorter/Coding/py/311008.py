import os
import shutil
from datetime import date

path = 'C:\\Users\\Dabba\\Desktop\\Sorter\\TEST2'
os.chdir(path)
files = os.listdir(path)


today = date.today()
year = today.strftime('%Y')
month = today.strftime('%m').zfill(2)
day = today.strftime('%d').zfill(2)

dt_path= f'{year}{month}'
# print(dt_path)




ext = set()



for file in files:
    name, file_ext = os.path.splitext(file)
    file_ext = file_ext[1:]
    if file_ext != '':
        ext.add(file_ext)



''' Test this

for file in files:
    name, file_ext = os.path.splitext(file)
    file_ext = file_ext[1:]
    if file_ext != '':
        ext.add(file_ext)
        if os.path.exists(path + '/' + ext + '/' dt_path):
        shutil.move(path + '/' + file, path + '/' + ext + '/' + dt_path + '/' file)
    else:
        os.makedirs(path + '/' + ext + '/' + dt_path):
        shutil.move(path + '/' + file, path + '/' + ext + '/' dt_path + '/' + file)'''


print(ext)








# for file in files:
#     if os.path.exists(path + '/' + ext + '/' dt_path):
#         shutil.move(path + '/' + file, path + '/' + ext + '/' + dt_path + '/' file)
#     else:
#         os.makedirs(path + '/' + ext + '/' + dt_path):
#         shutil.move(path + '/' + file, path + '/' + ext + '/' dt_path + '/' + file)







'''if not os.path.exists(dt_path):
    os.mkdir(dt_path)
else:
    print(f'{dt_path} Already Exits.')'''



'''for n in enumerate(files):
    print(n[1:])'''



'''for subfolder in ext:
    if not os.path.exists(subfolder):
        os.makedirs(subfolder + '/' + dt_path)

    else:
        print(f'Subfolder of {ext} Already Exists.')'''




