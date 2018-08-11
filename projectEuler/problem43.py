# https://projecteuler.net/problem=43

from itertools import permutations

def getPandigital():
    su = 0
    print(len(list(permutations(['1','2','3','4','5','6','7','8','9','0']))))
    for i in permutations(['1','2','3','4','5','6','7','8','9','0']):
        s = ''.join(i)
        if s[0] != '0':
            if int(s[1:4]) % 2 == 0 and int(s[2:5]) % 3 == 0 and \
            int(s[3:6]) % 5 == 0 and int(s[4:7]) % 7 == 0 and \
            int(s[5:8]) % 11 == 0 and int(s[6:9]) % 13 == 0 and\
            int(s[7:10]) % 17 == 0:
                su += int(s)
    return su
print(getPandigital())
