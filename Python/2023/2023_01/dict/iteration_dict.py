# -*- coding: utf-8 -*-
"""PyDict.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VWOcynHAjtUK4sZ-GTA85Y5xbY8UYLtR
"""

dict = {
    '1': ['A', 'B'],
    '2': ['C', 'D']
}
# update the dict
k3 = {3: ['E', 'F']}

dict.update(k3)

pair = []

for key in dict.keys():
    for value in (dict.get(key)):
        pair.append(f'{key}{value}')

print(pair)
# create a string
print(''.join(pair))