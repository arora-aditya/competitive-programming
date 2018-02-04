class Solution(object):
    def firstUniqChar(self, s):
        """
        https://leetcode.com/problems/first-unique-character-in-a-string/description/
        :type s: str
        :rtype: int
        """
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
