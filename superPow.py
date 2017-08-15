from math import fmod
def superPow(a, b):
    """
    :type a: int
    :type b: List[int]
    :rtype: int
    """
    if a % 1337 == 0:
        return 0
    count = 1
    length = len(b)
    for i in range(length):
        count *= fmod(a**(b[i]*(10**(length-i-1))),1337)
    return int(count%1337)

print(superPow(2,[1,0]))

