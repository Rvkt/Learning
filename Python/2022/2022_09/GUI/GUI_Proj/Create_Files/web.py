import os

dstn = input('Destination Path:\n')
os.chdir(dstn)

key = input('Enter Project Name: ')

try:
    if not os.path.exists(key):
        print(f'{key} is created in the {dstn}.')
        os.mkdir(key)
except:
    print('Already Exists!!')

os.chdir(key)

dict = {key: ['html', 'css', 'js']}
for key in dict.keys():
    for value in (dict.get(key)):
        # print(f'{key}.{value}')
        with open(f'{key}.{value}', 'w'):
            print(f'{key}.{value} is Created.')
            pass