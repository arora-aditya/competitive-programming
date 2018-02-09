class Solution(object):
    def judgeSquareSum(self, c):
        """
        https://leetcode.com/problems/sum-of-square-numbers/description/
        :type c: int
        :rtype: bool
        """
        def is_square(N):
            return int(N**.5)**2 == N

        return any(is_square(c - a*a)
                    for a in range(int(c**.5) + 1))
