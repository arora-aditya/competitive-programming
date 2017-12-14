class Solution:
    def superPow(self, a, b):
        """
        https://leetcode.com/problems/super-pow/description/
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        k = 1
        m = {0:a%1337}
        st = "{0:b}".format(int(''.join(map(str, b))))
        for i,ch in enumerate(st[::-1]):
            if ch == "1":
                save = i
                while i not in m.keys():
                    i -= 1
                while save != i:
                    m[i+1] = m[i]*m[i]%1337
                    i += 1
                k *= m[save]
                k = k%1337
        return k





        
