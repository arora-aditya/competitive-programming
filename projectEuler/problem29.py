# https://projecteuler.net/problem=29

di = {}
count = 0
for a in range(2,101):
  for b in range(2,101):
    k = a**b
    if k not in di:
      di[k] = 1
      count += 1
print(count)
