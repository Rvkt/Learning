import string
import random


text = {
    'lower': random.choice('abcdefghijklmnopqrstuvwxyz'),
    'upper': random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
    'digit': random.choice('string.digits'),
    'symbol': random.choice('!@$%&*?')
}


Chars = ('lower', 'upper',  'digit', 'symbol')


a = text['lower']
b = text['symbol']
c = text['upper']
d = text['digit']


p1 = (a,b,c,d)
p2 = (c,d,a,b)
p3 = (d,a,b,c)
p4 = (a,b,c,d)


print(p1, p2, p3, p4)