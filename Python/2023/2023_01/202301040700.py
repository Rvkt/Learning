# -*- coding: utf-8 -*-
"""202301040700.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ds4JSWpqKyX3qsdGZ3oF1s6bfxIZMJJs

String
"""

txt= 'rohan-is-a-good-boy'

txt1= txt.split('-')

print(txt1)

TXT='HELLO%WORLD%%HELLO%'
# COUNT:- ”%”


x = TXT.count("%")

print(x)

# 1):- FIND ALL THE OCCURRENCES OF OF GIVEN SUBSTRING IN THE PROVIDED STRING

STR='TIGER IS A GOOD DOG AND DOG ARE FRIENDLY IN NATURE'
SUBSTRING="DOG"

print(STR.count(SUBSTRING))

# 2):- CREATE A STRING MADE OF THE FIRST, MIDDLE AND LAST CHARACTER:-

TXT="Hello World Welcome"

print(f'{TXT[0]}{TXT[2]}{TXT[4]}')

# CREATE A STRING MADE OF THE LAST CHARACTERS:-

TXT1="HELLO"
TXT2="WORLD"



print(TXT[0] + "" + TXT1[1] + "" + TXT2[-1])

# 3):-  CREATE A STRING MADE OF THE LAST CHARACTERS:-
TXT="HELLO"
TXT1="WORLD"

print(TXT[-1] + '' + TXT1[-1])

txt="jidfhuishdifnasdnfjhaiuenfijnadjksbnfjibdsafndsafindsanfnkjsanfjnbdasjfnjansjkdfnjibnreibfinrvdsnfnijerifnger"

print(len(txt))



print(txt[int(len(txt))//2 + 1])
print(txt[int(len(txt))//2])
print(txt[len(txt)//2])