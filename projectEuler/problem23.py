# https://projecteuler.net/problem=23
def genDiv(n):
    i = 2
    upper = n
    total = 1
    while i < upper:
        if n%i == 0:
            upper = n/i
            total += upper
            if upper != i: total += i
        i += 1
    return total


def isabundant(n): return genDiv(n) > n
lAbundants = [x for x in range(12, 28123) if isabundant(x) == True]
dAbundants = {x:x for x in lAbundants}

su = 1
for i in range(2, 28123):
    flag = True
    for k in lAbundants:
        if k < i:
            if (i-k) in dAbundants:
                flag = False
                break
        else : break
    if flag == True: su += i

print(su)
