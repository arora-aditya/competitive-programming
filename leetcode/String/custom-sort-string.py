class Solution:
    def customSortString(self, S, T):
        """
        https://leetcode.com/problems/custom-sort-string/description/
        :type S: str
        :type T: str
        :rtype: str
        """

        di = {"q": float('inf'),"w": float('inf'),"e": float('inf'),"r": float('inf'),"t": float('inf'),"y": float('inf'),"u": float('inf'),"i": float('inf'),"o": float('inf'),"p": float('inf'),"a": float('inf'),"s": float('inf'),"d": float('inf'),"f": float('inf'),"g": float('inf'),"h": float('inf'),"j": float('inf'),"k": float('inf'),"l": float('inf'),"z": float('inf'),"x": float('inf'),"c": float('inf'),"v": float('inf'),"b": float('inf'),"n": float('inf'),"m": float('inf')}
        for i in range(len(S)):
            di[S[i]] = i
        return ''.join(sorted(T, key=lambda x: di[x]))
