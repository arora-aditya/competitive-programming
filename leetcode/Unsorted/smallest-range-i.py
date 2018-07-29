class Solution:
    def smallestRangeI(self, A, K):
        """
        https://leetcode.com/problems/smallest-range-i/description/
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        ma, mi = -float('inf'), float('inf')
        for i in A:
            ma = max(ma, i)
            mi = min(mi, i)
        return max(ma - mi - 2 *K, 0)
