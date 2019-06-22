from collections import defaultdict
class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        di = defaultdict(set)
        i = 0
        for word1, word2 in pairs:
            di[word1].add(i)
            di[word2].add(i)
            i += 1
        # print(di)
        for i in range(len(words1)):
            word1 = words1[i]
            word2 = words2[i]
            if len(di[word1] & di[word2]) == 0 and word1 != word2:
                return False
        return True