class Solution(object):
    def maxProduct(self, words):
        """
        https://leetcode.com/problems/maximum-product-of-word-lengths/description/
        :type words: List[str]
        :rtype: int
        """
        words.sort(key = len)
        words = words[::-1]
        se = [set(word) for word in words]
        ma = 0
        for i in range(len(words)):
            for j in range(len(words)):
                if len(se[j] - se[i]) == len(se[j]) and len(se[i] - se[j]) == len(se[i]) and i != j:
                    # print(words[i],words[j])
                    ma = max(ma,len(words[j])*len(words[i]))
                if len(words[i]) * len(words[j]) < ma:
                    break
            if len(words[i]) * len(words[0]) < ma:
                    break
        return ma
