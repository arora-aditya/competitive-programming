class Solution:
    def getModifiedArray(self, length, updates):
        """
        https://leetcode.com/problems/range-addition/description/
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        ans = [0] * (length+1)
        for start, end, inc in updates:
            ans[start] += inc
            ans[end+1] -= inc
        for i in range(1,len(ans)):
            ans[i] += ans[i-1]
        ans.pop()
        return ans
