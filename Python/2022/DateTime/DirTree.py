import os

path = os.getcwd()

dstn = os.chdir(path)




if not os.path.exists ('year_month'):
    os.mkdir('year_month')

elif os.path.exists('year_month'):
    os.chdir('year_month')
    print(os.getcwd())
    if not os.path.exists('date_hour_minutes'):
        os.mkdir('date_hour_minutes')
        os.chdir('date_hour_minutes')
        print(os.getcwd())
    else:
        if not os.path.exists('date_hour_minutes'):
            os.mkdir('date_hour_minutes')
            os.chdir('date_hour_minutes')
            print(os.getcwd())


    
   
    
    




