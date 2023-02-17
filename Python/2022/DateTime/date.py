import calendar, os
from datetime import date, datetime

now = datetime.now()
yr = now.strftime('%Y')
day = now.strftime('%d').zfill(2)
month = calendar.month_abbr[1:]
print(month)
yymm = []


if not os.path.exists(yr):
    os.mkdir(yr)
    os.chdir(yr)
    print(f'cwd: {os.getcwd()}')
else:
    os.chdir(yr)
    print(f'cwd: {os.getcwd()}')


for i in month:
    yymm.append(f'{yr}{i.upper()}')
    
for i in yymm:
    print(i)

for i in yymm:
    try:
        os.mkdir(i)
        print(f'{i} is created in the {os.getcwd()}')
    except:
        print(f"{i} Already Exists!!")
        

  


"""class MyNumbers:
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

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

"""