import random
def modulo (a, b, c):
    result = 1;
    while b != 0:
        if (b&1):
          result *= a;
          result %= c;

        b >>=1 ;
        a *= a;
        a %= c;


    return result;


def isPrime(n):
    if n==2:
        return 1
    for i in range(10):
        x = random.randint(0,1)%n
        if (x==0 or x==1):
            x+=1
        if (modulo(x,n-1,n)!=1):
            return 0


    return 1;

i = 1
n = 2
while i < 10010:
    if(isPrime(n)):
        print(i,n)
        i+=1
    n+=1
print(n)
