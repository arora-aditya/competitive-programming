class Solution(object):
    def findLengthOfLCIS(self, a):
        """
        https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
        :type nums: List[int]
        :rtype: int
        """
        le = len(a)
        if le <= 1:
            return le
        i, j = 0, 1
        maSe = 1
        while j < le:
            if a[j] > a[j-1]:
                j += 1
            else:
                maSe = max(maSe, j - i)
                i = j
                j += 1
        return max(maSe, j-i)
