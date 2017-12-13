from itertools import permutations
def countArrangement(N):
    """
    https://leetcode.com/problems/beautiful-arrangement/description/
    :type N: int
    :rtype: int
    """
    def isArrangement(x):
        for i in range(len(x),2):
            if (x[i]%(i+1) != 0 and (i+1)%x[i]!=0):
                return False
        for i in range(1,len(x),2):
            if (x[i]%(i+1) != 0 and (i+1)%x[i]!=0):
                return False
        return True
    k = 0
    for i in permutations(list(range(1,N+1,1))):
        if isArrangement(i):
            k = k + 1
    return k


for i in range(2,16):
    print(countArrangement(i))
