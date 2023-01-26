import random
import array

MAX_LEN = int(input('Password length: '))

UPPERCASE_CHAR = ['Y', '{', 'Z', 'w', '(', 'x', 'U', '!', 'V', 's', '@', 't', 'Q', '#', 'R', 'o', '$', 'p', 'M', '%', 'N', 'k', '^', 'l', 'I', '&', 'J', 'g', '*', 'h', 'E', '?', 'F', 'c', ')', 'd', 'A', '}', 'B', 'a', '[', 'b', 'C', '<', 'D', 'e', '?', 'f', 'G', '*', 'H', 'i', '&', 'j', 'K', '^', 'L', 'm', '%', 'n', 'O', '$', 'P', 'q', '#', 'r', 'S', '@', 'T', 'u', '!', 'v', 'W', '>', 'X', 'y', ']', 'z']

LOWERCASE_CHAR = ['a', '[', 'b', 'C', '<', 'D', 'e', '?', 'f', 'G', '*', 'H', 'i', '&', 'j', 'K', '^', 'L', 'm', '%', 'n', 'O', '$', 'P', 'q', '#', 'r', 'S', '@', 'T', 'u', '!', 'v', 'W', '>', 'X', 'y', ']', 'z', 'Y', '{', 'Z', 'w', '(', 'x', 'U', '!', 'V', 's', '@', 't', 'Q', '#', 'R', 'o', '$', 'p', 'M', '%', 'N', 'k', '^', 'l', 'I', '&', 'J', 'g', '*', 'h', 'E', '?', 'F', 'c', ')', 'd', 'A', '}', 'B']

DIGITS = ['2', '1', '0', '?', '1', '*', '2', '*', '3', '&', '4', '^', '5', '%', '6', '$', '7', '#', '8', '@', '9', '!', '0', '9', '8']

SYMBOLS = ['2', '1', '0', '!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', ')', '?', '0', '9', '8']

COMBINED_LIST = UPPERCASE_CHAR + LOWERCASE_CHAR + DIGITS + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPPERCASE_CHAR)
rand_lower = random.choice(LOWERCASE_CHAR)
rand_symbol = random.choice(SYMBOLS)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
# print(temp_pass)
for x in range(MAX_LEN - 4):
	temp_pass = temp_pass + random.choice(COMBINED_LIST)
	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
		password = password + x
print(password)