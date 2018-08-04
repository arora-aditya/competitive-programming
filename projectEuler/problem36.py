# https://projecteuler.net/problem=36

def doubleBasePalindromes():
    su = 0
    for i in range(1000000):
        st = bin(i)[2:]
        si = str(i)
        if si == si[::-1] and st == st[::-1]:
            su += i
    return su

print(doubleBasePalindromes())
