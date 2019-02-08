class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        # https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/
        if not M or not M[0]:
            return 0

        maxCount = 0
        m, n = len(M), len(M[0])
        row = [0] * m
        col = [0] * n
        # slope approach
        diag = [0] * (m+n-1)
        antiDiag = [0] * (m+n-1)
        for i in range(m):
            for j in range(n):
                if M[i][j] == 0:
                    row[i] = 0
                    col[j] = 0
                    diag[i-j+n-1] = 0
                    antiDiag[i+j] = 0
                else:
                    row[i] += 1
                    col[j] += 1
                    diag[i-j+n-1] += 1
                    antiDiag[i+j] += 1
                    maxCount = max(maxCount, row[i], col[j], diag[i-j+n-1], antiDiag[i+j])
        return maxCount

    def dpApproach_longestLine(self, M: List[List[int]]) -> int:
        m, n = len(M), len(M[0]) if M else 0
        dp = [[[0,0,0,0] if M[j][i] == 0 else [1,1,1,1] for i in range(n)] for j in range(m)]
        # h,v,d,ad
        if m > 0 and n > 0:
            ma = max(dp[0][0])
        else:
            ma = 0
        for i in range(m):
            for j in range(n):
                if M[i][j] == 0:
                    continue
                else:
                    if i == 0 and j == 0:
                        continue
                    elif i == 0:
                        dp[i][j] = [max(dp[i][j][0], dp[i][j-1][0]+1),
                                    1,
                                    1,
                                    1,
                                   ]
                    elif j == 0:
                        dp[i][j] = [1,
                                    max(dp[i][j][1], dp[i-1][j][1]+1),
                                    1,
                                    1
                                   ]
                    elif i == m-1 and j == n-1:
                        dp[i][j] = [max(dp[i][j][0], dp[i][j-1][0]+1),
                                    max(dp[i][j][1], dp[i-1][j][1]+1),
                                    max(dp[i][j][2], dp[i-1][j-1][2]+1),
                                    1
                                   ]
                    elif j == n-1:
                        dp[i][j] = [max(dp[i][j][0], dp[i][j-1][0]+1),
                                    max(dp[i][j][1], dp[i-1][j][1]+1),
                                    max(dp[i][j][2], dp[i+1][j-1][2]+1),
                                    1
                                   ]
                    elif i == m-1:
                        dp[i][j] = [max(dp[i][j][0], dp[i][j-1][0]+1),
                                    max(dp[i][j][1], dp[i-1][j][1]+1),
                                    max(dp[i][j][2], dp[i-1][j-1][2]+1),
                                    1
                                   ]

                    else:
                        dp[i][j] = [max(dp[i][j][0], dp[i][j-1][0]+1),
                                    max(dp[i][j][1], dp[i-1][j][1]+1),
                                    max(dp[i][j][2], dp[i-1][j-1][2]+1),
                                    1,
                                   ]
                    ma = max(ma, max(dp[i][j]))
        for i in range(1, m):
            for j in range(n-2, -1, -1):
                if M[i][j]:
                    dp[i][j][3] = max(dp[i][j][3], dp[i-1][j+1][3]+1)
                    ma = max(ma, max(dp[i][j]))

        return ma
