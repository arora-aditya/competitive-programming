class Solution:
    def toGoatLatin(self, S):
        """
        https://leetcode.com/problems/goat-latin/description/
        :type S: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        words = S.split(" ")
        for i,v in enumerate(words):
            if v[0] in vowels:
                words[i] += "ma" + 'a'* (i + 1)
            else:
                temp = words[i][0]
                words[i] = words[i][1:] + temp  + "ma" + 'a'* (i + 1)

        answer =' '.join(words)

        return answer
