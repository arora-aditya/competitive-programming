from collections import defaultdict
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        https://leetcode.com/problems/degree-of-an-array/description/
        :type nums: List[int]
        :rtype: int
        """
        map = defaultdict(list)
        for i in range(len(nums)):
            map[nums[i]].append(i)
        return min((-len(list), list[-1] - list[0] + 1) for list in map.values())[1]
        
