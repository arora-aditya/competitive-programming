class Solution(object):
    def isSubsequence(self, s, t):
        """
        https://leetcode.com/problems/is-subsequence/
        :type s: str
        :type t: str
        :rtype: bool
        """
        index = 0
        for c in s:
            index = t.find(c,index)
            if index == -1:
                return False
            index += 1
        return True
