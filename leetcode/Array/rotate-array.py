class Solution(object):
    def rotate(self, nums, k):
        """
        https://leetcode.com/problems/rotate-array/description/
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        le = len(nums)
        nums[:] = nums[le-k:]+nums[:le-k]
