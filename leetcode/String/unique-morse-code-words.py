class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        https://leetcode.com/problems/unique-morse-code-words/description/
        :type words: List[str]
        :rtype: int
        """
        a = set()
        for word in words:
            k = ""
            mapping = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            for i in s:
                k += mapping[ord(i) - 97]
            a.add(k)
        return len(a)
