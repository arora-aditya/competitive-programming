class Solution(object):
    def topKFrequent(self, words, k):
        """
        https://leetcode.com/problems/top-k-frequent-words/description/
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        frequencies = {}
        for word in words:
            if word in frequencies:
                frequencies[word] += 1
            else:
                frequencies[word] = 1
        uniqueWords = frequencies.keys()
        uniqueWords.sort()
        uniqueWords = sorted(uniqueWords, key = lambda x: frequencies[x], reverse = True)
        return uniqueWords[:k]
            
