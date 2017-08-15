from itertools import permutations

def getPermutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    i=1
    numString=""
    while i <= n:
        numString += str(i)
        i += 1
        
    perms = list(permutations(numString))
    return str(''.join(perms[k-1]))
print(getPermutation(3,4))
