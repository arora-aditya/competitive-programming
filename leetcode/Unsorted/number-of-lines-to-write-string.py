class Solution:
    def numberOfLines(self, widths, S):
        """
        https://leetcode.com/problems/number-of-lines-to-write-string/description/
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lineCount, currentLine = 0, 0
        for i in S:
            if widths[ord(i) - 97] > 100 - currentLine:
                lineCount += 1
                currentLine = widths[ord(i) - 97]
            else:
                currentLine += widths[ord(i) - 97]
        if currentLine:
            lineCount += 1
        return [lineCount, currentLine]
