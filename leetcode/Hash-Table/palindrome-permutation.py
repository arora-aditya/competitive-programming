class Solution(object):
    def canPermutePalindrome(self, s):
        """
        https://leetcode.com/problems/palindrome-permutation/description/
        :type s: str
        :rtype: bool
        """
        di = {}
        for char in s:
            di[char] = di.get(char, 0) + 1
        flag = True
        for i in di:
            if di[i]%2 == 1:
                if flag:
                    flag = False
                else:
                    return False
        return True
