import string

upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
symbol = string.punctuation
digit = string.digits


print(upper_case)
print(lower_case)
print(symbol)
print(digit)

import random
import array
import string
MAX_LEN = int(input('Password length: '))

UPPERCASE_CHAR = string.ascii_uppercase
LOWERCASE_CHAR = string.ascii_lowercase
SYMBOLS = string.punctuation
DIGITS = string.digits

COMBINED_LIST = UPPERCASE_CHAR + LOWERCASE_CHAR + DIGITS + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPPERCASE_CHAR)
rand_lower = random.choice(LOWERCASE_CHAR)
rand_symbol = random.choice(SYMBOLS)

temp_pass = rand_upper + rand_lower + rand_digit + rand_symbol
# print(temp_pass)
for x in range(MAX_LEN - 4):
	temp_pass = temp_pass + random.choice(COMBINED_LIST)
	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
		password = password + x
print(password)

import random
Chars = "Az<2By[1Cx{0Dw(9Ev!8Fu@7Gt#6Hs$5Ir%4Jq^3Kp&2Lo*1Mn?0Nm?0Ol*1Pk&2Qj^3Ri%4Sh$5Tg#6Uf@7Ve!8Wd)9Xc}0Yb]1Za>2"
while 1:
    password_len = input("Password length: ")
    if password_len == 'q':
        print('---- Programme Terminated ----')
        break
    else:
        password_count = int(input("How many passwords would you like : "))
    for x in range(0, password_count):
        password = ""
        for x in range(0, int(password_len)):
            password_char = random.choice(Chars)
            password      = password + password_char
        print(f"\tYour Password: {password}",)

import random, sys

Chars = 'a[bC<De?fG*Hi&jK^Lm%nO$Pq#rS@Tu!vW>Xy]zY{Zw(xU!Vs@tQ#Ro$pM%Nk^lI&Jg*hE?Fc)dA}BY{Zw(xU!Vs@tQ#Ro$pM%Nk^lI&Jg*hE?Fc)dA}Ba[bC<De?fG*Hi&jK^Lm%nO$Pq#rS@Tu!vW>Xy]z210?1*2*3&4^5%6$7#8@9!098210!1@2#3$4%5^6&7*8(9)?098'

while 1:
    password_len = input("What length would you like your password to be : ")
    if password_len == 'q':
        print('---- Programme Terminated ----')
        # sys.exit()
        break
    else:
        password_count = int(input("How many passwords would you like : "))
    
    for x in range(0, password_count):
        password = ""
        for x in range(0, int(password_len)):
            password_char = random.choice(Chars)
            password      = password + password_char
        print("\t Your Password : " , password)

import hashlib
m = hashlib.sha256()
str1 = 'Nobody inspects the spamming repetition'
str_salt = 'sine'
str_pepper = 'Q'
main = f'{str1} {str_salt} {str_pepper}'
# m.update(b"Nobody inspects the spamming repetition")
m.update(b"main")
# m.digest()
# m.hexdigest()

print(f'{m.digest()}\n{m.hexdigest()}')

import hashlib
hashlib.sha224(b"Nobody inspects the spamming repetition").hexdigest()

h = hashlib.new('sha256')
str1 = 'Nobody inspects the spamming repetition'
str_salt = 'sine'
str_pepper = 'Q'
main = f'{str1} {str_salt} {str_pepper}'

h.update(b"main")
h.hexdigest()

from hashlib import blake2b
h = blake2b()
h.update(b'hello123')
h.hexdigest()