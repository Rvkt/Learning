while 1:
    s = input('Enter Text: \n')
    if s == 'q':
        exit()

    capt1 = s[0::2].capitalize()
    capt2 = s[1::3].capitalize()
    capt3 = s[2::4].capitalize()
    capt4 = s[3::5].capitalize()

    capt = f'{capt1}!7{capt2}@5{capt3}#3{capt4}$2'
    print(capt)
    print(len(capt))