from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            print('here')
            return False
        di = {}
        for i in s1:
            di[i] = di.get(i, 0) + 1
        ls1 = len(s1)
        di_sliding = {}
        for i in range(ls1):
            di_sliding[s2[i]] = di_sliding.get(s2[i], 0) + 1
        if di_sliding == di:
            return True
        for i in range(ls1, len(s2)):

            di_sliding[s2[i]] = di_sliding.get(s2[i], 0) + 1
            di_sliding[s2[i - ls1]] -= 1
            if di_sliding[s2[i - ls1]] == 0:
                del di_sliding[s2[i - ls1]]
            if di_sliding == di:
                return True
        return False
        
    def TimeLimitExceeded_checkInclusion((self, s1: str, s2: str) -> bool:
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        S1 = list(permutations(s1))
        for i in range(len(S1)):
            S1[i] = ''.join(S1[i])
        for i in S1:
            if i in s2:
                return True
        return False
