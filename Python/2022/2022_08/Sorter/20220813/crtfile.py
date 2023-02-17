import os

dstn = input('Destination Path:\n')
os.chdir(dstn)


for i in range(1):
    with open(f'test{i}.doc', 'w'):
        pass
    with open(f'test{i}.txt', 'w'):
        pass
    with open(f'test{i}.pdf', 'w'):
        pass
    with open(f'test{i}.ppt', 'w'):
        pass