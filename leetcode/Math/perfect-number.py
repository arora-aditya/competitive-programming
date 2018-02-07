class Solution(object):
    def checkPerfectNumber(self, num):
        """
        https://leetcode.com/problems/perfect-number/description/
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        ans, sqrt = 0, int(num ** 0.5)
        ans = sum(i + num//i for i in range(1, sqrt+1) if not num % i)
        if num == sqrt ** 2: ans -= sqrt
        return ans - num == num
