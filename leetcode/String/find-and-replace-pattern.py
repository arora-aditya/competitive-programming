class Solution:
    def mapping(self, word1, word2):
        di = {}
        for i in range(len(word1)):
            if word1[i] in di and word2[i] != di[word1[i]]:
                return False
            else:
                di[word1[i]] = word2[i]
        word2, word1 = word1, word2
        di = {}
        for i in range(len(word1)):
            if word1[i] in di and word2[i] != di[word1[i]]:
                return False
            else:
                di[word1[i]] = word2[i]
        return True

    def findAndReplacePattern(self, words, pattern):
        """
        https://leetcode.com/problems/find-and-replace-pattern/description/
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        a = []
        for i in words:
            if self.mapping(i, pattern):
                a.append(i)
        return a
