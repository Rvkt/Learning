n = int(input('Enter the number of the rows: '))
symbol = '•'
num = 1
str = input('Enter String: ')

print('                 ')
print('Floyd\'s Triangle')
print('                 ')
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(symbol, end=' ')
    print()

print('                              ')
print('Floyd\'s Triangle with numbers')
print('                              ')
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(num, end=' ')
        num = num + 1
    print()
