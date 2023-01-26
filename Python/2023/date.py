from datetime import date, datetime

now = datetime.now()
dt_str = now.strftime('%Y_%m_%d')

print('Date:\t', dt_str)