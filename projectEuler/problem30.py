# https://projecteuler.net/problem=30

def checkSum(n):
  return sum(int(c)**5 for c in str(n)) == n

su = 0
for i in range(2, 1000000):
  if(checkSum(i)):
    print(i, checkSum(i))
    su += i
print(su)
