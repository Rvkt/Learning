lowercase = 'ZyXwVuTsRqPoNmLkJiHgFeDcBa'
uppercase = 'AbCdEfGhIjKlMnOpQrStUvWxYz'
digits    = '1<2[3{4(050)6}7]8>9'
symbols = '?*&^%$#@!@#$%^&*?'
'''!<@[#{$(%)^}&]*>?'''

def stringToList(lowercase):
   return list(lowercase)
def stringToList(uppercase):
   return list(uppercase)
def stringToList(digits):
   return list(digits)
def stringToList(symbols):
   return list(symbols)

with open("Stringlist.txt",'w',encoding = 'utf-8') as f:
   f.write(f'Uppercase = {stringToList(uppercase)}\nLowercase = {stringToList(lowercase)}\nDigits = {stringToList(digits)}\nSymbol = {stringToList(symbols)}')