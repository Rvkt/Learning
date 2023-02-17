# C:\Users\Dabba\Desktop\Cloud\2022\202207290011\test

import os
import shutil



path = os.chdir ('C:\\Users\\Dabba\\Desktop\\Cloud\\2022\\202207290011\\test')

# Path('Copied').mkdir(exist_ok=True)

try:
    if not os.path.exists('copied'):
        os.mkdir('copied')
except:
    pass


for file in os.listdir(path):
    shutil.copy(file, 'copied')