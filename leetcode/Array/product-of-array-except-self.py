class Solution(object):
    def productExceptSelf(self, nums):
        """
        https://leetcode.com/problems/product-of-array-except-self/description/
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)
        leftsum = 1
        rightsum = 1
        for i in range(len(nums)):
            result[i] *= leftsum
            result[len(nums)-i-1] *= rightsum
            leftsum *= nums[i]
            rightsum *= nums[len(nums)-i-1]
        return result
