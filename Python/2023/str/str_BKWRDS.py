string = 'abcdefghijklmnopqrstuvwxyz'


# Reverse the given string
def bkwrds(x):
    return x[::-1]

print(f'{string}')
print(f'{bkwrds(string)}')
print(f'Palindrome of the given string: \n{string[0:-1:]}{bkwrds(string)}')