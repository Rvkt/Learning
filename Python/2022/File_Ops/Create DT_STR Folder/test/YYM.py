import os

path = input('Enter Path: ')
os.chdir(path)

year = input('Enter Year: ')

if not os.path.exists(year):
    os.mkdir(year)

for file in os.listdir(path):
    if file != year:
        pass
    else:
        if file == year:
            # print('Exists')
            os.chdir(year)

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