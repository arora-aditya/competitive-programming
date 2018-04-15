# https://projecteuler.net/problem=34

def fact1(n):
  k = 1
  for i in range(2,n+1):
    k *= i
  return k

fact = {'0':1}
for i in range(1,10):
  fact[str(i)] = fact1(i)
print(fact)

def checkSum(n):
  return sum(fact[c] for c in str(n)) == n

l = []
for i in range(3,100000000):
  if checkSum(i):
    l.append(i)
print(l, sum(l))
