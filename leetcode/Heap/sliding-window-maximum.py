class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        https://leetcode.com/problems/sliding-window-maximum/description/
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        li = []
        for i in range(len(nums)-k+1):
            if i == i + k:
                continue
            li.append(max(nums[i:i+k]))
        return li
