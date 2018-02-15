class Solution(object):
    def missingNumber(self, nums):
        """
        https://leetcode.com/problems/missing-number/description/
        :type nums: List[int]
        :rtype: int
        """
        su, le = 0, 0
        for i in nums:
            su += i
            le += 1
        return int((le*(le+1))/2 - su)
            
