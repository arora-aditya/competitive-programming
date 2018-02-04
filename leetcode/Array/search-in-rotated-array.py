class Solution(object):
    def search(self, nums, target):
        """
        https://leetcode.com/problems/search-in-rotated-sorted-array/description/
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except ValueError:
            return -1
