from datetime import datetime
now = datetime.now()

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