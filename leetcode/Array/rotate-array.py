class Solution(object):
    def rotate(self,nums, k):
        """
        https://leetcode.com/problems/rotate-array
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]

