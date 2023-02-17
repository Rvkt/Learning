import string
import random


text = {
    'lower': random.choice('abcdefghijklmnopqrstuvwxyz'),
    'upper': random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
    'digit': random.choice('0123456789'),
    'symbol': random.choice('!@$%&*?')
}

Chars1 = text['lower'],text['symbol'],text['upper'],text['digit']
txt1 = (''.join(Chars1))


Chars2 = text['lower'],text['symbol'],text['upper'],text['digit']
txt2 = (''.join(Chars2))


Chars3 = text['lower'],text['symbol'],text['upper'],text['digit']
txt3 = (''.join(Chars3))


Chars4 = text['lower'],text['symbol'],text['upper'],text['digit']
txt4 = (''.join(Chars4))


Chars = (f'{txt1}{txt2}{txt3}{txt4}')
Chars = ''.join(Chars)


print(Chars)