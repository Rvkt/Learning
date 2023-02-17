import random, sys

Chars = 'a[bC<De?fG*Hi&jK^Lm%nO$Pq#rS@Tu!vW>Xy]zY{Zw(xU!Vs@tQ#Ro$pM%Nk^lI&Jg*hE?Fc)dA}BY{Zw(xU!Vs@tQ#Ro$pM%Nk^lI&Jg*hE?Fc)dA}Ba[bC<De?fG*Hi&jK^Lm%nO$Pq#rS@Tu!vW>Xy]z210?1*2*3&4^5%6$7#8@9!098210!1@2#3$4%5^6&7*8(9)?098'

while 1:
    password_len = input("Password Length: ")
    if password_len == 'q':
        sys.exit()
    else:
        password_count = int(input("No. of Passwords: "))
    
    for x in range(0, password_count):
        password = ""
        for x in range(0, int(password_len)):
            password_char = random.choice(Chars)
            password      = password + password_char
        print("\t Your Password : " , password)