class Solution:
    def maximalSquare(self, M: List[List[str]]) -> int:
        # https://leetcode.com/problems/maximal-square/
        if len(M) == 0:
            return 0
        R, C = len(M), len(M[0])
        S = [[0 for k in range(C)] for l in range(R)] 
        S[0] = [int(x) for x in M[0]]
        ma = max(S[0])
        for i in range(1, R): 
            S[i][0] = int(M[i][0])
            ma = max(S[i][0], ma)
            for j in range(1, C): 
                if (M[i][j] == "1"): 
                    S[i][j] = min(S[i][j-1], S[i-1][j], 
                                S[i-1][j-1]) + 1
                    ma = max(S[i][j], ma)
                else: 
                    S[i][j] = 0
        return ma*ma