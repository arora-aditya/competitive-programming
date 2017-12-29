class Solution(object):
    def arrayPairSum(self, nums):
        """
        https://leetcode.com/problems/array-partition-i/description/
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        sum = 0
        for i in range(0,len(nums),2):
            sum += nums[i]
        return sum
