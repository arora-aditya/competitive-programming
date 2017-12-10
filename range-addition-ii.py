class Solution:
    def maxCount(self, m, n, ops):
        """
        https://leetcode.com/problems/range-addition-ii/description/
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        for op in ops:
            m = min(m,op[0])
            n = min(n,op[1])
        return m*n
