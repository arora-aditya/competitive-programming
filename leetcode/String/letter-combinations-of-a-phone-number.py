class Solution:
    def letterCombinations(self, digits):
        """
        https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'1':'','2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        if digits == '':
            return []
        else:
            ans = mapping[digits[0]]
            # print(ans)
            for i in range(1,len(digits)):
                l = []
                for j in mapping[digits[i]]:
                    for k in ans:
                        l.append(k+j)
                ans = l
                # print(ans)
        return ans
