class Solution(object):
    def twoSum(self, nums, target):
        """
        # https://leetcode.com/problems/two-sum/
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]