class Solution:
    def countPrimeSetBits(self, L, R):
        """
        https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/
        :type L: int
        :type R: int
        :rtype: int
        """

        def isprime(n):
            """Returns True if n is prime."""
            if n == 1:
                return False
            if n == 2:
                return True
            if n == 3:
                return True
            if n % 2 == 0:
                return False
            if n % 3 == 0:
                return False

            i = 5
            w = 2

            while i * i <= n:
                if n % i == 0:
                    return False

                i += w
                w = 6 - w

            return True
        dct = {}
        counter = 0
        for i in range(L,R+1):
            cnt = "{0:b}".format(i).count('1')
            dct[cnt] = dct.get(cnt,0) + 1
            # print("{0:b}".format(i), cnt, dct[cnt])
        for i in dct:
            if isprime(int(i)):
                counter += dct[i]
                # print(i, counter)
        # print(dct, counter)
        return counter
