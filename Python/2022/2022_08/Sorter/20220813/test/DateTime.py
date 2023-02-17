from datetime import datetime

now = datetime.now()
 # current date and time

# func = input(str('  Enter Function:\n'))

def weekday():

    weekday_sv = now.strftime('%a')
    print('Weekday, short version:', weekday_sv )
    
    weekday_fv = now.strftime('%A')
    print('Weekday, full version:', weekday_fv )
    
    weekday_index = now.strftime('%w')
    print('Weekday, as index:', weekday_index )

weekday()

def month():

    month_sv = now.strftime('%b')
    print(month_sv)
    
    month_fv = now.strftime('%B')
    print(month_fv)
    
    month_nm = now.strftime('%m')
    print(month_nm)

weekday()

def dayNum():

    dayNum = now.strftime('%d')
    print(f'Day of the month: {dayNum}')
    
    dayNum = now.strftime('%j')
    print(f'Day of the year: {dayNum}')


weekday()








year = now.strftime("%Y")
print("Year Full:", year)

year = now.strftime("%y")
print("Year Short:", year)

month = now.strftime("%m")
print("Month:", month)

month = now.strftime("%b")
print("Month:", month.upper())

month = now.strftime("%B")
print("Month:", month.upper())

dayNum = now.strftime("%d")
print("Day:", dayNum)

dayName = now.strftime("%a")
print("Day:", dayName)

dayName = now.strftime("%A")
print("Day:", dayName)

hour = now.strftime("%H")
print("Hour:", hour)

minutes = now.strftime("%M")
print("Minutes:", minutes)

seconds = now.strftime("%S")
print("Seconds:", seconds)

amPM = now.strftime("%p")
print('Period:', amPM)







'''

# print(now.strftime('%m').zfill(4))
# Output --> 0007

'''
