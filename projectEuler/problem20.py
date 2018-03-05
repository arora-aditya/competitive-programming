# https://projecteuler.net/problem=19

k = 1
for i in range(1,101):
  k *= i
su = 0
while k:
  su += k%10
  k = k//10
print(su)
