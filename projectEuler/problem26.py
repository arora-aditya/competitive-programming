# https://projecteuler.net/problem=26

import itertools
def countMax(n):
  seen = {}
  x = 1
  for i in itertools.count():
    if x in seen:
      return i - seen[x]
    else:
      seen[x] = i
      x = x * 10 % n

ma = -1
d = -1
for i in range(2,1000):
#   print(1/i)
  if ma < countMax(i):
    d = i
    ma = countMax(i)
print(d,ma)
