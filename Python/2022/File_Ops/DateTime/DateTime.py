from datetime import date, datetime

now = datetime.now()

# nt = '\n\t'

day_name1, day_name2, day_name3 = now.strftime('%a'), now.strftime('%A'), now.strftime('%w')
print(f'Weekday short version is {day_name1}, Weekday full version is {day_name2}, and Weekday as a number 0-6, 0 is Sunday, {day_name3}.')

day_num1, day_num2 = now.strftime('%d'), now.strftime('%j')
print(f'Day of month is {day_num1} and Day number of year {day_num2}.')

mon1, mon2, mon3  = now.strftime('%b'), now.strftime('%B'), now.strftime('%m')
print(f'Month short is {mon1}, Month full version is {mon2} and month as number is {mon3}')

century, year1, year2 = now.strftime('%C'), now.strftime('%y'), now.strftime('%Y')
print(f'Century is {century}, year is {year1} and year in full version {year2}')

hour1, hour2, ampm = now.strftime('%H'), now.strftime('%I').zfill(2), now.strftime('%p')
print(f'Hour in 24 hour format is {hour1}, hour in 12 hour format is {hour2} and time period is {ampm}.')

min = now.strftime('%M').zfill(2)
print(f'Minutes is {min}.')

sec = now.strftime('%S').zfill(2)
print(f'Seconds is {sec}.')

msec = now.strftime('%f').zfill(2)
print(f'Miliseconds is {msec}.')

dttm, dt, tm = now.strftime('%c'), now.strftime('%x'), now.strftime('%X')
print(f'local version of data and time is {dttm}, local version of date is {dt} and local version of time is {tm}')