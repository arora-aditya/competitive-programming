from math import log10
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
        ans = 0
        for num in nums:
            l = log10(num)
            if pow(10, l) == num and int(l) % 2 == 1:
                ans += 1
            elif int(l + 1) % 2 == 0:
                ans += 1
            # print(l)
        return ans