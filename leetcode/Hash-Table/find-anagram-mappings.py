class Solution:
    def anagramMappings(self, A, B):
        """
        https://leetcode.com/problems/find-anagram-mappings/description/
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dc = {}
        for i in range(len(B)):
            dc[B[i]] = i
        li = []
        for i in A:
            li.append(dc[i])
        return li
