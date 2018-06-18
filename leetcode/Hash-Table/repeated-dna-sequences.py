class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        https://leetcode.com/problems/repeated-dna-sequences/description/
        :type s: str
        :rtype: List[str]
        """
        di = {}
        for i in range(len(s)-9):
            if s[i:i+10] in di:
                di[s[i:i+10]] += 1
            else:
                di[s[i:i+10]] = 1
        ans = []
        for i in di:
            if di[i] > 1:
                ans.append(i)
        return ans
