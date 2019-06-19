from math import log10

class Solution:
    def isArmstrong(self, N: int) -> bool:
        # https://leetcode.com/problems/armstrong-number/
        st = str(N)
        k = len(st)
        su = 0
        for num in st:
            su += pow(int(num), k) 
            if su > N:
                return False
        return su == N
        