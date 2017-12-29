class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        https://leetcode.com/problems/count-numbers-with-unique-digits/description/
        :type n: int
        :rtype: int
        """
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        count = 1
        prod = 1
        
        for i in range(min(n,10)):
            prod *= choices[i]
            count += prod
        return count
