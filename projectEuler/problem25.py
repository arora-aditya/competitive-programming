# https://projecteuler.net/problem=25

F1 = 1
F2 = 1
F = F1 + F2
count = 2
while len(str(F)) < 1000:
  F = F1 + F2
  count += 1
  #   print(F, count)
  F1 = F2
  F2 = F
print(count)
