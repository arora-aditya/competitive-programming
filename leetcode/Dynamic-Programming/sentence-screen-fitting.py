class Solution:
    def TLE_wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        le = len(sentence)
        dp = [0]*le
        for i in range(le):
            dp[i] = len(sentence[i])
        # print(dp)
        r, c = rows, cols
        i = 0
        while r > 0:
            l = 0
            while c >= l:
                # print('C1', i,l,r,c)
                l += dp[i%le]
                if l < c:
                    l += 1
                i += 1
                # print('C2', i,l,r,c)
            # print('R', i,l,r,c)
            i -= 1
            r -= 1
        return i//le