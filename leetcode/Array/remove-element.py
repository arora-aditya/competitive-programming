class Solution:
    def removeElement(self, nums, val):
        """
        https://leetcode.com/problems/remove-element/description/
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cnt = nums.count(val)
        for i in range(cnt):
            nums.remove(val)
        return len(nums)
