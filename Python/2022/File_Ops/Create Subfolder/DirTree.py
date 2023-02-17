import os

path = os.getcwd()

dstn = os.chdir(path)

if not os.path.exists ('year_month'):
    os.mkdir('year_month')
    os.chdir('year_month')
    
else os.path.exists('year_month'):
    if not os.path.exists('date_hour_minutes'):
        os.mkdir('date_hour_minutes')