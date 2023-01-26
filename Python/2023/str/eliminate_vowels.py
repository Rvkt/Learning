string = 'helloJohn'

str_vowels = ['a', 'e', 'i', 'o', 'u']

def eliminate_vowels(string):
    for i in string:
        if i.lower() in str_vowels:
            string = string.replace(i, '')
    print(string)

eliminate_vowels(string)