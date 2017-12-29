class Solution(object):
    def findLHS(self, nums):
        """
        https://leetcode.com/problems/longest-harmonious-subsequence/
        :type nums: List[int]
        :rtype: int
        """
        le = 0
        numDict = {}
        for x in nums:
            numDict[x] = numDict.get(x, 0) + 1
        for i in numDict:
            if i+1 in numDict:
                le=max(numDict[i] + numDict[i+1],le)
        return le
