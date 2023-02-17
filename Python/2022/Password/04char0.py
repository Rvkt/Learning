import string
import random


lower = random.choice(string.ascii_lowercase)
upper = random.choice(string.ascii_uppercase)
digits = random.choice(string.digits)


text = {
    'lower': random.choice('abcdefghijklmnopqrstuvwxyz'),
    'upper': random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
    'digit': random.choice('string.digits'),
    'symbol': random.choice('!@$%&*?')
}


a = text['lower']
b = text['symbol']
c = text['upper']
d = text['digit']


p1 = (a,b,c,d)


print(p1)