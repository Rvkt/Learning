from datetime import datetime

x = datetime.now()

print('Century: ' + x.strftime("%C"))
print('Year, short version, without century: ' + x.strftime("%y").zfill(2))
print('Year, full version: ' + x.strftime("%Y"))


print('Month name, short version: ' + x.strftime("%b"))
print('Month name, full version: ' + x.strftime("%B"))
print('Month as a number: ' + x.strftime("%m").zfill(2))


print('Day: ' + x.strftime("%d").zfill(2))
print('Day number of year 001-366: ' + x.strftime("%j"))


print('Weekday, short version: ' + x.strftime("%a"))
print('Weekday, full version: ' + x.strftime("%A"))
print('Weekday as a number 0-6, 0 is Sunday: ' + x.strftime("%w"))


print('Hour 00-23: ' + x.strftime("%H"))
print('Hour 00-12: ' + x.strftime("%I"))
print('AM/PM: ' + x.strftime("%p"))


print('Minute 00-59: ' + x.strftime("%M").zfill(2))


print('Seconds 00-59: ' + x.strftime("%S").zfill(2))


print('Microsecond: ' + x.strftime("%f"))


