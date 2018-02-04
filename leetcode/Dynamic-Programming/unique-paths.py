class Solution:
    def uniquePaths(self, m, n):
        """
        https://leetcode.com/problems/unique-paths/description/
        :type m: int
        :type n: int
        :rtype: int
        """
        ma, mi = max(m-1,n-1) , min(m-1,n-1)
        su = m + n - 2
        # print(su, ma, mi)
        k = 1
        for i in range(su,ma,-1):
            k = k * i
            # print(k)
        for i in range(1,mi+1):
            k = k / i
            # print(k)
        return int(k)
