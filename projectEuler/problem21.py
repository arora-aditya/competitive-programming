# https://projecteuler.net/problem=21

def genDiv(k):
  re = 1
  for i in range(2, int(pow(k,0.5))+1):
    if k%i == 0:
      re += i
      re += int(k/i)
  return re

su = 0
di = {}
for i in range(0,10001):
  di[i] = genDiv(i)
for i in di:
  if di[i] in di and i == di[di[i]] and i != di[i]:
    print(i,di[i])
    su += i
print(su)
