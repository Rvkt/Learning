from datetime import datetime
now = datetime.now()

ymd = []
month_day = []
year = int(now.strftime('%Y'))

# month_curr = now.strftime('%b').upper()
month_input = input('Enter Month: ')


month31 = ['JAN', 'MAR', 'MAY', 'JUL', 'AUG', 'OCT', 'DEC']
month30 = ['NOV', 'APR', 'JUN', 'SEP']

for m in month31:
    if month_input.upper() == m:
            for i in range(1, 32):
                month_day.append(f'{m}{str(i).zfill(2)}')
    
    elif month_input.upper() == 'FEB':
            if (year % 400 == 0) and (year % 100 == 0):
                if (year % 4 == 0) and (year % 100 != 0):
                    for i in range(1, 29):
                        month_day.append(f'FEB{str(i).zfill(2)}')
            else:
                for i in range(1, 28):
                    month_day.append(f'FEB{str(i).zfill(2)}')
    else:
        for m in month30:
            if month_input.upper() == m:
                for i in range(1, 31):
                    month_day.append(f'{m}{str(i).zfill(2)}')

print(month_day)