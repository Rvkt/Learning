from datetime import datetime
import os


now = datetime.now()
yr = now.strftime('%Y')
# print(year)
month = []
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


for x in iter(MyNumbers()):
    month.append(x)
# print(month)
for i in month:
    yymm.append(f'{yr}{i.upper()}')
# print(yymm)

if not os.path.exists(yr):
    os.mkdir(yr)
    os.chdir(yr)
    print(f'{yr} is created in the \n specified path.')
else:
    pass

for i in iter(yymm):
    # print(i)
    os.mkdir(i)
    print(f'{i} is created in \n {os.getcwd()}.')


