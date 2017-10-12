class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        https://leetcode.com/problems/baseball-game/description/
        """
        compiledList = []
        for i in ops:
            if i == "C":
                del compiledList[-1]
            elif i == "+":
                compiledList.append(compiledList[-1]+compiledList[-2])
            elif i == "D":
                compiledList.append(2 * compiledList[-1])
            else:
                compiledList.append(int(i))
        return sum(compiledList)
