import os

path = input('Enter Path: ')
os.chdir(path)

year = input('Enter Year: ')

dirName = f'{year}'

if not os.path.exists(dirName):
    os.mkdir(dirName)

for file in os.listdir(path):
    if file != dirName:
        pass
    else:
        if file == dirName:
            # print('Exists')
            os.chdir(dirName)

dict = {
    year : ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
}

yymm = []

for key in dict.keys():
    for value in (dict.get(key)):
        yymm.append(f'{key}_{value}')

for i in yymm:
    if not os.path.exists(i):
        os.mkdir(i)
        print(f'{i} is created in {os.getcwd()}')