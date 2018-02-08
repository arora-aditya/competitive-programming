import operator
class Solution(object):
    def frequencySort(self, s):
        """
        https://leetcode.com/problems/sort-characters-by-frequency/description/
        :type s: str
        :rtype: str
        """
        d = {}
        for i in s:
            d[i] = d.get(i,0) + 1
        k = ""
        for i in sorted(d, key=d.get, reverse=True):
            k += i * d[i]
        return k
