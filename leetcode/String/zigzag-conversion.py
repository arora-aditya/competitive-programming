class Solution:
    def convert(self, s, numRows):
        """
        https://leetcode.com/problems/zigzag-conversion/description/
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows<=1: return s
        ans=[""]*numRows
        i=0
        for c in s:
            ans[i]+=c
            if i==numRows-1:
                d=-1
            if i==0:
                d=1
            i+=d
        return ''.join(ans)
