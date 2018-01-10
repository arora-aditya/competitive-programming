class Solution:
    def moveZeroes(self, nums):
        """
        https://leetcode.com/problems/move-zeroes/description/
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        le = len(nums)
        cnt = 0
        i = 0
        while i < le:
            if nums[i] == 0:
                nums.pop(i)
                cnt += 1
                le -= 1
            else:
                i += 1
        nums.extend([0]*cnt)
