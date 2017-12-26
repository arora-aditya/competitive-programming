class Solution(object):
    def convertToBase7(self, num):
        """
        https://leetcode.com/problems/base-7/
        :type num: int
        :rtype: str
        """
        base7 = "0123456"
        if num == 0:
            return "0"
        rl = ""
        flag = ""
        if num < 0:
            flag = "-"
            num = num * -1
        while num > 0:
            rl += base7[num%7]
            num //= 7
        return flag + rl[::-1]
