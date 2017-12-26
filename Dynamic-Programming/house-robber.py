class Solution:
    """
    https://leetcode.com/problems/house-robber/#/description
    :type nums: List[int]
    :rtype: int
    """
    def __init__(self,nums):
        self.nums=nums

    def rob(self, nums):

        last, now = 0, 0

        for i in nums:
            print(i,"\t",last,"\t",now,"\t",last+i)
            last, now = now, max(last + i, now)

        return now
