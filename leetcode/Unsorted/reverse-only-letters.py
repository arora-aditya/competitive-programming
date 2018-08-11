class Solution:
    def reverseOnlyLetters(self, S):
        """
        https://leetcode.com/problems/reverse-only-letters/description/
        :type S: str
        :rtype: str
        """
        if S == "":
            return ""
        S = list(S)
        i, j = 0, len(S) - 1
        while i < j:
            if S[i].isalpha() == False:
                i += 1
            elif S[j].isalpha() == False:
                j -= 1
            else:
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
        return ''.join(S)
