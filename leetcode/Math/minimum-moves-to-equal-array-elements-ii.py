class Solution(object):
    def minMoves2(self, nums):
        """
        https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        median = nums[len(nums) / 2]
        res = 0
        for n in nums:
            res += abs(n-median)
        return res
