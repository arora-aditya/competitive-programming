class Solution(object):
    def matrixScore(self, A):
        """
        https://leetcode.com/problems/score-after-flipping-matrix/description/
        :type A: List[List[int]]
        :rtype: int
        """
        R, C = len(A), len(A[0])
        ans = 0
        for c in range(C):
            col = 0
            for r in range(R):
                col += A[r][c] ^ A[r][0]
            ans += max(col, R - col) * (1 << (C - 1 - c))
        return ans
