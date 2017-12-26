class Solution(object):
    def findTheDifference(self, s, t):
        """
        https://leetcode.com/problems/find-the-difference/description/
        :type s: str
        :type t: str
        :rtype: str
        """
        def convert_to_dict(d):
            x = {}
            for char in d:
                x[char] = x.get(char,0) + 1
            return x
        
        def subtract_dict(d,k):
            l = {}
            if len(d) > len(k):
                t = k
                k = d
                d = t
            for char in k.keys():
                l[char] = abs(k[char] - d.get(char,0))
            for char in l:
                if l[char] != 0:
                    return char
        y = convert_to_dict(s)
        z = convert_to_dict(t)
        return subtract_dict(y, z)
