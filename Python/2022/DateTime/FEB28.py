from datetime import datetime
now = datetime.now()
yr = now.strftime('%y')
feb = []
year = int(now.strftime('%Y'))

def leap_yr():
    if (year % 400 == 0) and (year % 100 == 0):
        if (year % 4 == 0) and (year % 100 != 0):
                for i in range(1, 29):
                    feb.append(f'{yr}FEB{str(i).zfill(2)}')
    else:
        for i in range(1, 28):
            feb.append(f'{yr}FEB{str(i).zfill(2)}')
leap_yr()
print(feb)