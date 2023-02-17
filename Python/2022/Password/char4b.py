import random


text = {
    'lower': random.choice('abcdefghijklmnopqrstuvwxyz'),
    'upper': random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
    'digit': random.choice('0123456789'),
    'symbol': random.choice('!@$%&*?')
}

Chars1 = text['lower'],text['symbol'],text['upper'],text['digit']
Chars1 = (''.join(Chars1))


Chars2 = text['lower'],text['symbol'],text['upper'],text['digit']
Chars2 = (''.join(Chars2))


Chars3 = text['lower'],text['symbol'],text['upper'],text['digit']
Chars3 = (''.join(Chars3))


Chars4 = text['lower'],text['symbol'],text['upper'],text['digit']
Chars4 = (''.join(Chars4))


Chars = (f'{Chars1}{Chars2}{Chars3}{Chars4}')
Chars = ' '.join(Chars)


print(Chars) 


