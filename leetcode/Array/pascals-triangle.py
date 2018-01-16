class Solution:
    def generate(self, numRows):
        """
        https://leetcode.com/problems/pascals-triangle/description/
        :type numRows: int
        :rtype: List[List[int]]
        """
        li = []
        save = {0:1, 1:1, 2:2, 3:6, 4:24}
        def factorial(n, saved=save):
            if n in save:
                return save[n]
            ma = max(saved.keys())
            k = saved[ma]
            for i in range(ma+1, n+1):
                k = k * i
                saved[i] = k
            return k
        # print(factorial(10,saved),saved)
        def nCr(n,r):
            if n == r:
                return 1
            elif n-r == 1 or r == 1:
                return n
            else:
                # assert(int(factorial(n)/(factorial(n-r)*factorial(r))) == factorial(n)/(factorial(n-r)*factorial(r)))
                return int(factorial(n)/(factorial(n-r)*factorial(r)))

        for i in range(numRows):
            li.append([])
            for j in range(i+1):
                # print(i,j,nCr(i,j))
                li[-1].append(nCr(i,j))
            # print(li)
        # print(li)
        # print(save)
        return li
