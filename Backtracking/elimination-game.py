class Solution(object):
    def lastRemaining(self, n):
        """
        https://leetcode.com/problems/elimination-game/#/description
        :type n: int
        :rtype: int
        """
        if n == 3 or n == 2:
            return 2
        elif n == 1:
            return 1
        else:
            base = 4 * self.lastRemaining(n/4)
            if n%4 == 0 or n%4 == 1:
                return base - 2
            else:
                return base
