class Solution(object):
    def minimumTotal(self, triangle):
        """
        https://leetcode.com/problems/triangle/description/
        :type triangle: List[List[int]]
        :rtype: int
        """
        lastRow = triangle[-1]

        for row in reversed(triangle[:-1]):
            tempRow = row[:]
            for i in range(0,len(row)):
                tempRow[i] += min(lastRow[i], lastRow[i+1])
            lastRow = tempRow
        return lastRow[0]
