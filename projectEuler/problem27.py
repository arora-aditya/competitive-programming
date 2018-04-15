# https://projecteuler.net/problem=27

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False
    return True

primes = {1:1}
for i in range(2,10000):
  if isPrime(i):
    primes[i] = 1

def f(a,b):
  i = 0
  while i*i + a*i + b in primes:
    #     print(i*i + a*i + b)
    i += 1
  return i

print(f(-79, 1601))

ma = 0
A = 0
B = 0
for a in range(-1001,1000):
  for b in range(-1002,1001):
    k = f(a,b)
    if ma < k:
      ma = k
      A = a
      B = b

print(ma, A, B)
