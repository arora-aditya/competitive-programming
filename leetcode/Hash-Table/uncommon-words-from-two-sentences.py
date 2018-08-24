class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        https://leetcode.com/problems/uncommon-words-from-two-sentences/description/
        :type A: str
        :type B: str
        :rtype: List[str]
        """

        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1
        return [word for word in count if count[word] == 1]
