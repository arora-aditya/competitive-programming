class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        # https://leetcode.com/problems/n-repeated-element-in-size-2n-array
        di = {}
        for i in A:
            if i in di:
                return i
            else:
                di[i] = 1
