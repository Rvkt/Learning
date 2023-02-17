while 1:
    
    txt1 = input('Enter Text: \n')
    
     txt2 = txt1[-2::-1]
    
    join_txt = (txt1, txt2)
    join_txt = ''.join(join_txt)
    print(join_txt)