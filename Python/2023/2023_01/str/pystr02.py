# -*- coding: utf-8 -*-
"""PyStr02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ten8s2PGn5bVmsbBdFecN6qPnHRCni3A

The syntax of the **center()** method is:

*str.center(width, [fillchar])*

**String to Binary**
"""

import math

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

string = '31'


print(f'String in binary: {toBinary(string)}')

test_str = "H"

# using join() + ord() + format()
# Converting String to binary
res = ''.join(format(ord(i), '08b') for i in test_str)

print("The string after binary conversion : " + str(res))

test_str = "hello"
print(f'Given string: {test_str}')
# using join() + bytearray() + format()
# Converting String to binary
res = ''.join(format(i, '08b') for i in bytearray(test_str, encoding ='utf-8'))

print("\nThe string after binary conversion : " + str(res))

bnum = res

b = int(bnum, 2)
hdnum = hex(b)
print("\nEquivalent Hexadecimal Value = ", hdnum)

string = " String is Centered "

# returns the centered padded string of length 24 
new_string = string.center(30, '-')

print(new_string)

# Output: ----- String is Centered -----

text = "String is Centered"

# returns padded string by adding whitespace up to length 24
new_text = text.center(24)

print("Centered String: ", new_text)
print("", new_text)

"""**Join String**

"""

str1 = 'ABC'
str2 = '123'

def join_str1():
    output = []
    i = 0

    for a in str1:
        output.append(a)
        while 1< len(str2):
            output.append(str2[i])
            i += 1
            break

    str_output = ''.join(output)
    print(f'Output: {str_output}')

join_str1()

str1 = 'ABC'
str2 = '123'

def join_str2():
    output2 = []
    str_output2 = ''.join(output2)
    idx = 0

    for i in str1:
        output2.append(str1[idx])
        output2.append(str2[idx])
        idx += 1

    print(f'output: {str_output2}')

join_str2()

def join_str3():
    output3 = ''

    for i in range(len(str1)):
        output3 += str1[i] + str2[i]
    output3.strip()

    print(f'Output: {output3}')

join_str3()

def join_str4():
    output4 = ''

    for (a, b) in zip(str1, str2):
        output4 += a + b

    print(f'Output: {output4}')

join_str4()

# Replace string char It's syntax is: str.replace(old, new [, count])
 

text = 'IMG20210604072119'

'''replaced_text = text.replace('img', 'vlg')
print(replaced_text)'''

def replace():
    text_replace = text.replace('IMG', 'VLG')
    print(text_replace)

replace()

song = 'cold, cold heart'

# replacing 'cold' with 'hurt'
print(song.replace('cold', 'hurt'))

song = 'Let it be, let it be, let it be, let it be'

# replacing only two occurences of 'let'
print(song.replace('let', "don't let", 2))

song = 'cold, cold heart'
replaced_song = song.replace('o', 'e')

# The original string is unchanged
print('Original string:', song)

print('Replaced string:', replaced_song)

song = 'let it be, let it be, let it be'

# maximum of 0 substring is replaced
# returns copy of the original string
print(song.replace('let', 'so', 0))

"""**Python String find()** The syntax of the find() method is: *str.find(sub[, start[, end]] )*"""

message = 'Python is afun programming language'

# check the index of 'fun'
print(message.find('fun'))

# Output: 12

if message.find('fun') != -1:
    print('Exists')

quote = 'Let it be, let it be, let it be'

# first occurance of 'let it'(case sensitive)
result = quote.find('let it')
print("Substring 'let it':", result)

# find returns -1 if substring not found
result = quote.find('small')
print("Substring 'small ':", result)

# How to use find()
if (quote.find('be,') != -1):
    print("Contains substring 'be,'")
else:
    print("Doesn't contain substring")

quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
print(quote.find('small things', 10))

# Substring is searched in ' small things with great love' 
print(quote.find('small things', 2))

# Substring is searched in 'hings with great lov'
print(quote.find('o small ', 10, -1))

# Substring is searched in 'll things with'
print(quote.find('things ', 6, 20))

txt = "Hello, welcome to my world."
search_str = input('Enter the string you want to search: ')
x = txt.find(search_str)
print(f'Exits at index: {x}' )