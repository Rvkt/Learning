def OddNum(a,b):
    odds = []
    if a % 2 == 0:
        a = a + 1
    for x in range(a, b, 2):
        odds.append(x)
    return odds

print(OddNum(1, 31))