class Solution(object):
    def findWords(self, words):
        """
        https://leetcode.com/problems/keyboard-row/description/
        :type words: List[str]
        :rtype: List[str]
        """
        row1=['Q','W','E','R','T','Y','U','I','O','P']
        row2=['A','S','D','F','G','H','J','K','L']
        row3=['Z','X','C','V','B','N','M']
        row_words=[]
        for word in words:
            count1=0
            count2=0
            count3=0
            for letter in word:
                if letter.upper() in row1:
                    count1 += 1
                elif letter.upper() in row2:
                    count2 += 1
                elif letter.upper() in row3:
                    count3 += 1
            if max(count1,count2,count3)==len(word):
                row_words.append(word)
        return row_words
