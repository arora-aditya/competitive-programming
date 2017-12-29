import math

# function to count the divisors
def countDivisors(n) :
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) :
        if (n % i == 0) :

            # If divisors are equal,
            # count only one
            if (n / i == i) :
                cnt = cnt + 1
            else : # Otherwise count both
                cnt = cnt + 2
    return cnt

i = 2
n = i*(i-1)/2
while True:
    an = 1
    n = n + i
    if countDivisors(n) > 500:
        print(i,countDivisors(n),n)
    i+=1
    # break;
