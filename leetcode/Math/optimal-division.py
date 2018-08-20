class Solution(object):
    def optimalDivision(self, nums):
        """
        https://leetcode.com/problems/optimal-division/description/
        :type nums: List[int]
        :rtype: str
        """
        A = map(str, nums)
        if len(A) <= 2: return '/'.join(A)
        return A[0] + '/(' + '/'.join(A[1:]) + ')'
