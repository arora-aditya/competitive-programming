# -*- coding: utf-8 -*-

# https://projecteuler.net/problem=17

# !pip install num2words
from num2words import num2words
cn = 0
for i in range(1,1001):
  k = num2words(i, lang='en_GB')
  for j in k:
    if j != ' ' and j != '-':
      cn += 1
print(cn)
