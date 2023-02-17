import os
import sys
import pkg_resources



dir_list = os.listdir(os.getcwd())


for dir in dir_list:
        if dir == 'env':
                os.chdir('./env/Scripts')
                print(os.getcwd())
                print(os.listdir())

