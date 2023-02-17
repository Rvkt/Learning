def EvenNum(a,b):
    if a % 2 == 1:
        a = a + 1
    odds = list(range(a,b,2))
    return odds

print(EvenNum(1, 31))