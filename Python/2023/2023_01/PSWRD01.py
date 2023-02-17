import random
import array

MAX_LEN = int(input('Password length: '))

UPPERCASE_CHAR = ['A', 'b', 'C', 'd', 'E', 'f', 'G', 'h', 'I', 'j', 'K', 'l', 'M', 'n', 'O', 'p', 'Q', 'r', 'S', 't', 'U', 'v', 'W', 'x', 'Y', 'z']
LOWERCASE_CHAR = ['Z', 'y', 'X', 'w', 'V', 'u', 'T', 's', 'R', 'q', 'P', 'o', 'N', 'm', 'L', 'k', 'J', 'i', 'H', 'g', 'F', 'e', 'D', 'c', 'B', 'a']
DIGITS = ['1', '<', '2', '[', '3', '{', '4', '(', '0', '5', '0', ')', '6', '}', '7', ']', '8', '>', '9']
SYMBOLS = ['?', '*', '&', '^', '%', '$', '#', '@', '!', '@', '#', '$', '%', '^', '&', '*', '?']

COMBINED_LIST = UPPERCASE_CHAR + LOWERCASE_CHAR + DIGITS + SYMBOLS
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPPERCASE_CHAR)
rand_lower = random.choice(LOWERCASE_CHAR)
rand_symbol = random.choice(SYMBOLS)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
for x in range(MAX_LEN - 4):
	temp_pass = temp_pass + random.choice(COMBINED_LIST)
	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
		password = password + x
print(password)

# with open("pswrd.txt",'w',encoding = 'utf-8') as f:
#    f.write(f'{password}')