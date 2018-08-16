class Solution(object):
    def multiply(self, num1, num2):
        """
        https://leetcode.com/problems/multiply-strings/description/
        :type num1: str
        :type num2: str
        :rtype: str
        """
        su = 0
        i = 0
        le2 = len(num2)
        while i < le2:
            su1 = 0
            a = int(num2[i])
            for j in num1:
                # print(a, j)
                su1 += int(j) * a
                su1 *= 10
            su += su1
            su *= 10
            i += 1
        return str(su/100)
