class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # return '-'.join(list(filter(None, [("").join(S.split("-")).upper()[::-1][i:i+K][::-1] for i in range(0, len(S), K)][::-1])))

        S = S.upper().replace('-','')
        size = len(S)
        s1 = K if size%K==0 else size%K
        res = S[:s1]
        while s1<size:
            res += '-'+S[s1:s1+K]
            s1 += K
        return res
