class Solution:
    def binaryGap(self, N):
        """
        https://leetcode.com/problems/binary-gap/description/
        :type N: int
        :rtype: int
        """
        s = bin(N)
        prev, ma = -1, 0
        for i in range(2, len(s)):
            if s[i] == '1':
                if prev == -1:
                    prev = i
                else:
                    ma = max(ma, i-prev)
                    prev = i
            # print(s[i], i, prev, ma)
        return ma
        
