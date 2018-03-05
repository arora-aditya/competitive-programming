# https://projecteuler.net/problem=19

import datetime
dt = datetime.datetime(1901, 1, 1)
end = datetime.datetime(2000, 12, 31)
step = datetime.timedelta(days=1)

cn = 0

while dt < end:
  if(dt.isoweekday() == 7 and dt.day == 1):
    cn += 1
  dt += step
print(cn)
