from datetime import datetime
import calendar

now = datetime.now()
yr = now.strftime('%Y')
month = []
mon2 = calendar.month_abbr[1:]
yymm = []
yymm2 = []

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
      
for x in iter(MyNumbers()):
    month.append(x)
for i in month:
    yymm.append(f'{yr}{i}')
for i in mon2:
  yymm2.append(f'{yr}{i.upper()}')


for i in iter(yymm):
    print(i)
print(' ')
for i in iter(yymm2):
    print(i)