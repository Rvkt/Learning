import random, array

CHAR_LEN = int(input('Password length: '))

uppercase = ['Z', 'y', 'X', 'w', 'V', 'u', 'T', 's', 'R', 'q', 'P', 'o', 'N', 'm', 'L', 'k', 'J', 'i', 'H', 'g', 'F', 'e', 'D', 'c', 'B', 'a', 'B', 'c', 'D', 'e', 'F', 'g', 'H', 'i', 'J', 'k', 'L', 'm', 'N', 'o', 'P', 'q', 'R', 's', 'T', 'u', 'V', 'w', 'X', 'y', 'Z']
lowercase = ['a', 'B', 'c', 'D', 'e', 'F', 'g', 'H', 'i', 'J', 'k', 'L', 'm', 'N', 'o', 'P', 'q', 'R', 's', 'T', 'u', 'V', 'w', 'X', 'y', 'Z', 'y', 'X', 'w', 'V', 'u', 'T', 's', 'R', 'q', 'P', 'o', 'N', 'm', 'L', 'k', 'J', 'i', 'H', 'g', 'F', 'e', 'D', 'c', 'B', 'a']
digits = ['1', '<', '2', '[', '3', '{', '4', '(', '0', '5', '0', ')', '6', '}', '7', ']', '8', '>', '9']
symbol = ['?', '*', '&', '^', '%', '$', '#', '@', '!', '@', '#', '$', '%', '^', '&', '*', '?']


COMBINED_LIST = uppercase + lowercase + digits + symbol

rand_digit = random.choice(digits)
rand_upper = random.choice(uppercase)
rand_lower = random.choice(lowercase)
rand_symbol = random.choice(symbol)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
# print(temp_pass)
for x in range(CHAR_LEN - 4):
	temp_pass = temp_pass + random.choice(COMBINED_LIST)
	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
		password = password + x
print(password)