import math

def prime_sieve(n, output={}):
    nroot = int(math.sqrt(n))
    sieve = list(range(n+1))
    sieve[1] = 0

    for i in range(2, nroot+1):
        if sieve[i] != 0:
            m = n/i - i
            sieve[i*i: n+1:i] = [0] * int(m+1)

    if type(output) == dict:
        pmap = {}
        for x in sieve:
            if x != 0:
                pmap[x] = True
        return pmap
    elif type(output) == list:
        return [x for x in sieve if x != 0]
    else:
        return None

def get_prime_factors(n, primelist = None):
    if primelist is None:
        primelist = prime_sieve(n,output=[])

    fs = {}
    for p in primelist:
        count = 0
        while n % p == 0:
            n /= p
            count += 1
        if count > 0:
            fs[p] = count

    return fs
ls = {}
for i in range(1,21):
    fs = get_prime_factors(i)
    print(fs)
    for i in fs:
        if ls.get(i,0) < fs[i]:
            ls[i] = fs[i]
num = 1
print(ls)
for i in ls:
    num = num * pow(i,ls[i])
for i in range(1,21):
    print(num%i, i, (num/i)%i)
print(num)
