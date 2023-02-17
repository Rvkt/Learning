from curses.ascii import isalpha, isdigit
from itertools import count


email = input('  Enter your Email:\n')

# usernm@g.in
# RegEx == (str1)@(str2).(2+char)


# r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
a,b,c=0,0,0

if len(email)>=6: #1
    if email[0].isalpha(): #2
        if ('@'in email) and (email.count()==1): #3
            if (email[-3]=='.') ^ (email[-4]=='.'): #4
                for char in email:
                    if char == char.isspace():
                        a=1
                    elif char.isalpha():
                        if char == char.upper():
                            b=1
                    elif char.isdigit():
                        continue
                    elif (char=='_') or (char=='.') or (char=='@'):
                        continue
                    else:
                        c = 1

                if a==1 or b==1 or c==1:
                    print('Wrong Email 5')
            else:
                print('Wrong Email 4')
        else:
            print('Wrong Email 3')
    else:
        print('Wrong Email 2')
else:
    print('Wrong Email 1')