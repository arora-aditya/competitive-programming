class Solution(object):
    def readBinaryWatch(self, num):
        """
        https://leetcode.com/problems/binary-watch/description/
        :type num: int
        :rtype: List[str]
        """
        return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == num]
        
