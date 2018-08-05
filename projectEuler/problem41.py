# https://projecteuler.net/problem=41

def isPandigital(x):
    x = str(x)
    for i in range(1, len(x)+1):
        if str(i) not in x:
            return False
    return True

def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def genPandigital():
    # starting from 7999999 instead of any of the 8 digit or 9 digit
    # pandigital, because all of those are multiples of 3 or 9
    # proof: sum of digits is ez to test for those numbers
    for i in range(7999999, 1, -1):
        if isPandigital(i):
            if isPrime(i):
                print(i)
                break
genPandigital()
