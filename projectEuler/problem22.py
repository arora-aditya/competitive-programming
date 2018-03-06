# https://projecteuler.net/problem=22

import urllib.request

st = "QWERTYUIOPASDFGHJKLZXCVBNM"
st = sorted(st)
di = {}
for i in range(len(st)):
  di[st[i]] = i+1


def word(k, di):
  su = 0
  for i in k:
    su += di[i]
  return su

file_url = 'https://projecteuler.net/project/resources/p022_names.txt'
names = sorted(urllib.request.urlopen(file_url).read().rstrip().decode('utf8').replace('"','').split(','))

names.index('COLIN')
su = 0
for i in range(len(names)):
  su += ((i+1) * word(names[i], di))
print(su)
