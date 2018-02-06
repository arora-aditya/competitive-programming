class Solution(object):
    def longestPalindrome(self, s):
        """
        https://leetcode.com/problems/longest-palindrome/description/
        :type s: str
        :rtype: int
        """
        di={}
        for char in s:
            di[char] = di.get(char,0) + 1
        flag = True
        length = 0
        for char in di:
            if di[char]%2 == 0:
                length += di[char]
            elif flag and di[char]%2==1:
                length += di[char]
                flag = False
            else:
                length += di[char]-1
        return length
