# https://projecteuler.net/problem=43

import math

def isPentagonal(x):
  r = pow(1 + 24 * x, 0.5)
  return r % 6 == 5


def answer():
  nums = [1, 5, 12];
  n, Pn = 4, 22
  while True:
      nums.append(Pn)
      n += 3
      Pn += n
      for i in nums[::-1]:
          if isPentagonal(abs(Pn - i)) and isPentagonal(i + Pn):
              print(Pn, i, Pn-i)
              print(nums)
              return

answer()
