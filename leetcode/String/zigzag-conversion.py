class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # https://leetcode.com/problems/zigzag-conversion/
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