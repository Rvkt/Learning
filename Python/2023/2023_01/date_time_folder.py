from datetime import date, datetime

now = datetime.now()

day_name1, day_name2, day_name3 = now.strftime('%a'), now.strftime('%A'), now.strftime('%w')
print(f'Weekday short version is {day_name1}\nWeekday full version is {day_name2}\nWeekday as a number 0-6, 0 is Sunday, {day_name3}.')

day_num1, day_num2 = now.strftime('%d'), now.strftime('%j')
print(f'Day of month is {day_num1}\nDay number of year {day_num2}.')

mon1, mon2, mon3  = now.strftime('%b'), now.strftime('%B'), now.strftime('%m')
print(f'Month short is {mon1}\nMonth full version is {mon2}\nmonth as number is {mon3}')

century, year1, year2 = now.strftime('%C'), now.strftime('%y'), now.strftime('%Y')
print(f'Century is {century}\nyear in short version {year1}\nyear in full version {year2}')

hour1, hour2, ampm = now.strftime('%H'), now.strftime('%I').zfill(2), now.strftime('%p')
print(f'Hour in 24 hour format is {hour1}\nhour in 12 hour format is {hour2}\ntime period is {ampm}.')

min = now.strftime('%M').zfill(2)
print(f'Minutes is {min}.')

print('')
sec = now.strftime('%S').zfill(2)
print(f'Seconds is {sec}.')
print('')

msec = now.strftime('%f').zfill(2)
print(f'Millisecond is {msec}.')
print('')

dttm, dt, tm = now.strftime('%c'), now.strftime('%x'), now.strftime('%X')
print(f'local version of data and time is {dttm}\nlocal version of date is {dt}\nlocal version of time is {tm}')
print('')

print(f'Date:    {day_name2} of {mon2} {day_num1.zfill(2)}, {year2}\nTime:    {hour2} : {min} : {sec} {ampm}')

from datetime import datetime

now = datetime.now()
yr = now.strftime('%Y')
yymm = []

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 12:
      x = self.a
      self.a += 1
      return str(x).zfill(2)
    else:
      raise StopIteration

for i in iter(MyNumbers()):
    yymm.append(f'{yr}{i}')

print(yymm)

ym = now.strftime('%y%b').upper()

ymd = []

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 31:
      x = self.a
      self.a += 1
      return str(x).zfill(2)
    else:
      raise StopIteration

for i in iter(MyNumbers()):
    ymd.append(f'{ym}{i}')

print(ymd)

from datetime import datetime
now = datetime.now()

month = now.strftime('%b').upper()

monthday = []

def feb28():
    for i in range(1, 29):
        print(i)
def feb27():
    for i in range(1, 28):
        print(i)
def day30():
    for i in range(1, 31):
        print(i)
def day31():
    for i in range(1, 32):
        monthday.append(f'{month}{str(i).zfill(2)}')
        

day31()
print(monthday)

def aug():
    for i in range(1, 32):
        print(f'{str(i).zfill(2)}')


txt = input('Enter month: ')

if txt.lower() == ('aug'):
    aug()

from datetime import date, datetime
now = datetime.now()
year = int(now.strftime('%Y'))

def leap_yr():
    if (year % 400 == 0) and (year % 100 == 0):
        print("{0} is a leap year, FEB28 Exists !!".format(year))

    elif (year % 4 == 0) and (year % 100 != 0):
        print("{0} is a leap year, FEB28 Exists !!".format(year))

    else:
        print("{0} is not a leap year, FEB28 Not Exists !!".format(year))

leap_yr()

year = int(now.strftime('%Y'))
feb = []

def feb28():
    for i in range(1, 29):
        feb.append(f'FEB{str(i).zfill(2)}')

def feb27():
    for i in range(1, 28):
        feb.append(f'FEB{str(i).zfill(2)}')

def leap_yr():
    if (year % 400 == 0) and (year % 100 == 0):
        if (year % 4 == 0) and (year % 100 != 0):
            return feb28()
    else:
        return feb27()
leap_yr()

print(feb)

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

year = input('Enter Year: ')
dict = {
    year : ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
}

for key in dict.keys():
    for month in (dict.get(key)):
        print(f'{key}{month}')

year = input('Enter Year: ')
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

dir_name = []
for m in month:
    dir_name.append(f'{year}{m}')
print(dir_name)

"""**Calender Module**"""

import calendar
from datetime import date, datetime

now = datetime.now()
year = now.strftime('%Y')
month_long = []

for i in range(1, 13):
    month_long.append(calendar.month_name[i]) # month_name is an array


for i in month_long:
    print(f'{i[0:3].upper()}_{i.upper()}')

month_short = calendar.month_abbr[1:]

# test = []
for i in month_short:
    print(f'{i}')
    # test.append(i) 
    # print(f'{year}{i.upper()}')
# print(test)

'''
Create directory with the name of last ten years.
'''

# import os
from datetime import date, datetime
now = datetime.now()
year = int(now.strftime('%Y'))
# path = input('Enter Path: ')
# os.chdir(path)
for y in range(year-10, year+1):
    print(y)
    #if not os.path.exists(y):
        #os.mkdir(str(y))
        #print(f'{y} created in {path}!')

yr = '2022'
# print(yr)

dict_mm = {
    yr : ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
}

for key in dict_mm.keys():
    for value in (dict_mm.get(key)):
        print(f'{key}{value}')

from datetime import datetime
now = datetime.now()
# yr = now.strftime('%y')
# feb = []
year = int(now.strftime('%Y'))
month_int = (now.strftime('%m').zfill(2))
month_str = now.strftime('%b')
# print(month_str)

dict_mmdd = {}

month_key = ''
day_list = []

key = {month_key: day_list}
dict.update(key)

'''

['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec']
['Feb']
['Apr', 'Jun', 'Sep', 'Nov',]

'''

MONTH31 = ['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec']
MONTH30 = ['Apr', 'Jun', 'Sep', 'Nov',]
FEB = []

for m in MONTH31 or m in MONTH30:
    if m == month_str:
        print(m)
    else:
        print('It must be feb.')
        

'''key_mmdd = {str(month).zfill(2): ['date']}
dict_mmdd.update(key_mmdd)
print(dict_mmdd)'''

list_mmdd = []

def DAY31():
    for m in MONTH31:
        # print(m)
        for i in range(1, 32):
            list_mmdd.append(f'{m}{str(i).zfill(2)}')
def leap_yr():
    if (year % 400 == 0) and (year % 100 == 0):
        if (year % 4 == 0) and (year % 100 != 0):
            print(f'Current Year is a leap year!')
            if month == '02':
                for i in range(1, 29):
                    FEB.append(f'{str(i).zfill(2)}')
    else:
        print(f'Current Year is not a leap year!')
        if month == '02':
            for i in range(1, 28):
                FEB.append(f'{str(i).zfill(2)}')

dict = {
    '1': ['A', 'B'],
    '2': ['C', 'D']
}
# update the dict
key3 = {3: ['E', 'F']}
dict.update(key3)

for key in dict.keys():
    for value in (dict.get(key)):
        print(f'{key}{value}')

from datetime import datetime
now = datetime.now()
year = int(now.strftime('%Y'))
month_int = (now.strftime('%m').zfill(2))
day = now.strftime('%d')
date_str = f'{year}_{month_int}_{day}'
print(date_str)