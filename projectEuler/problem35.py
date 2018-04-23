# https://projecteuler.net/problem=35

import itertools
primes = {1:1}
for i in range(2,1000000):
  if isPrime(i):
    primes[i] = 1

def check(n):
  ns = str(n)
  for j in range(0,len(ns)):
    if int(ns[j:] + ns[:j]) not in primes:
      return False
  return True

cn = 0
for i in primes:
  if check(i):
    cn += 1
