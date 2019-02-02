class Solution(object):
    def maxSubArray(self, nums):
        """
        https://leetcode.com/problems/maximum-subarray/description/
        :type nums: List[int]
        :rtype: int
        """
        sums = [0 for i in range(len(nums))]
        sums[0] = nums[0]
        max = sums[0]
        for i in range(1, len(sums)):
            sums[i] = sums[i-1] + nums[i] if sums[i-1] > 0 else nums[i]
            max = sums[i] if sums[i] > max else max
        return max
