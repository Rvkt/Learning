from datetime import date, datetime

now = datetime.now()

print('datetime module')
print('')
day_name1, day_name2, day_name3 = now.strftime('%a'), now.strftime('%A'), now.strftime('%w')
print(f'Weekday short version is {day_name1}\nWeekday full version is {day_name2}\nWeekday as a number 0-6, 0 is Sunday, {day_name3}.')

print('')
day_num1, day_num2 = now.strftime('%d'), now.strftime('%j')
print(f'Day of month is {day_num1}\nDay number of year {day_num2}.')
print('')

mon1, mon2, mon3  = now.strftime('%b'), now.strftime('%B'), now.strftime('%m')
print(f'Month short is {mon1}\nMonth full version is {mon2}\nmonth as number is {mon3}')
print('')

century, year1, year2 = now.strftime('%C'), now.strftime('%y'), now.strftime('%Y')
print(f'Century is {century}\nyear in short version {year1}\nyear in full version {year2}')
print('')

hour1, hour2, ampm = now.strftime('%H'), now.strftime('%I').zfill(2), now.strftime('%p')
print(f'Hour in 24 hour format is {hour1}\nhour in 12 hour format is {hour2}\ntime period is {ampm}.')

print('')
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