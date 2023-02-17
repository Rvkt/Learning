from datetime import date, datetime

now = datetime.now()
dt_str = now.strftime('%Y%m%d%H%M')

print(dt_str)