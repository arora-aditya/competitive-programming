from math import fmod
class Solution(object):
    def superPow(self, a, b):
        """
        https://leetcode.com/problems/super-pow/description/
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if a % 1337 == 0:
            return 0
        else:
            a = a%1337
        count = 1
        length = len(b)
        for i in range(length):
            count *= (a**(b[i]*(10**(length-i-1)))%1337)
        return int(fmod(count,1337))
