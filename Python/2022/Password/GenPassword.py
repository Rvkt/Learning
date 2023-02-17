import random

Chars = "Az<2By[1Cx{0Dw(9Ev!8Fu@7Gt#6Hs$5Ir%4Jq^3Kp&2Lo*1Mn?0Nm?0Ol*1Pk&2Qj^3Ri%4Sh$5Tg#6Uf@7Ve!8Wd)9Xc}0Yb]1Za>2"

while 1:
    password_len = input("Password Length: ")
    if password_len == 'q':
        print('---- Programme Terminated ----')
        break
    else:
        password_count = int(input("No. of Passwords: "))
    for x in range(0, password_count):
        password = ""
        for x in range(0, int(password_len)):
            password_char = random.choice(Chars)
            password      = password + password_char
        print(f"\tYour Password: {password}",)