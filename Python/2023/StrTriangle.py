str = input('Enter String: ').upper()
length_str = len(str)

print(' ')
print('String Right Angle triangle')
print(' ')

for row in range(length_str):
    for col in range(0, row+1):
        print(str[col], end=' ')
    print()






