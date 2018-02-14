class Solution(object):
    def dominantIndex(self, nums):
        """
        https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
        :type nums: List[int]
        :rtype: int
        """
        ma, idx = max(nums), -1
        for i in range(len(nums)):
            if nums[i] == ma:
                idx = i
            elif 2 * nums[i] > ma:
                return -1
        return idx
                
