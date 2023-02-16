import os
from datetime import date, datetime

now = datetime.now()
dt_str = now.strftime('%Y_%m_%d')

print(dt_str)

# if not os.path.exists(dt_str):
#     os.mkdir(dt_str)
# else:
#     print('Already Exits')
