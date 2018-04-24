class Solution(object):
    def flipAndInvertImage(self, A):
        """
        https://leetcode.com/problems/flipping-an-image/description/
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        def invert(i):
            return 0 if i == 1 else 1
        def flip(l):
            return list(map(invert, l))[::-1]
        return map(flip, A)
        
