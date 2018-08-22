class Solution(object):
    def similarRGB(self, color):
        """
        https://leetcode.com/problems/similar-rgb-color/description/
        :type color: str
        :rtype: str
        """
        def close(s):
            a,b = divmod(int(s, 16), 17)
            if b > 8: a += 1
            a = hex(a)[-1]
            return a + a
        return '#' + close(color[1:3]) + close(color[3:5]) + close(color[5:])
