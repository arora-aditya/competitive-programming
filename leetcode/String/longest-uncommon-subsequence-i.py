class Solution(object):
    def findLUSlength(self, a, b):
        """
        https://leetcode.com/problems/longest-uncommon-subsequence-i/description/
        :type a: str
        :type b: str
        :rtype: int
        """
        lea, leb = len(a), len(b)
        if lea != leb:
            return max(lea, leb)
        if a == b:
            return -1
        else:
            return lea
