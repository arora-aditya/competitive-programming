def countPrimes(n):
    isprime=[]
    for i in range(2,n):
        isprime[i]=1
    for i in range(2,n):
        if i * i > n:
            break
        if isprime[i] == 0:
            continue
        for j in range(i*i,n,i):
            isprime[j]=0
    count=0
    for i in range(n+1):
        if isprime[i]:
            count += 1
    return count

n=input()
print(countPrimes(int(n)))
