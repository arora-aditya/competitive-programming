class Solution:
    def sortArrayByParity(self, A):
        """
        https://leetcode.com/problems/sort-array-by-parity/description/
        :type A: List[int]
        :rtype: List[int]
        """
        even, odd = [], []
        for i in A:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even + odd
