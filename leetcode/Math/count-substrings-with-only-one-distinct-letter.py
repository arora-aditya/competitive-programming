class Solution:
    def countLetters(self, S: str) -> int:
        # https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/
        ans = 0
        i, j = 0, 0
        while j < len(S):
            if S[j] == S[i]:
                j += 1
            else:
                # print((j-i+1)*(j-i)/2, i, j)
                ans += (j-i+1)*(j-i)/2
                i = j
        # print((j-i+1)*(j-i)/2, i, j)
        ans += (j-i+1)*(j-i)/2
        return int(ans)