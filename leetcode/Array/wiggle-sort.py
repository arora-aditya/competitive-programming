class Solution:
    def wiggleSort(self, nums):
        """
        https://leetcode.com/problems/wiggle-sort/description/
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1,len(nums)-1,2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        
