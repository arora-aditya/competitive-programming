# https://projecteuler.net/problem=37

import itertools
primes = {}
for i in range(2,1000000):
  if isPrime(i):
    primes[i] = 1

def check2(n):
  ns = str(n)
  for j in range(1,len(ns)):
    if int(ns[:j]) not in primes:
      return False
  for j in range(1,len(ns)):
    if int(ns[j:]) not in primes:
      return False
  return True

l = []
for i in primes:
  if check2(i):
    l.append(i)
print(sum(l[4:]))
