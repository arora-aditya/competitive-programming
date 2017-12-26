class Solution(object):
    def solveEquation(self, equation):
        """
        https://leetcode.com/problems/solve-the-equation/description/
        :type equation: str
        :rtype: str
        """
        parts = equation.split('=')
        left = self.parsePart(parts[0])
        right = self.parsePart(parts[1])

        coff = left[1] - right[1]
        num = right[0] - left[0]

        if coff == num == 0:
            return "Infinite solutions"
        elif coff == 0 and num != 0:
            return "No solution"
        else:
            val = num / coff
            assert(val == int(val))
            return 'x=' + str(val)

    def parsePart(self, part):
        if part[0] != '-':
            part = '+' + part
        part = part.replace('+x','+1x').replace('-x','-1x')

        num_total = 0
        coff_total = 0

        num = 0
        sign = 1

        for c in part:
            if c == '+' or c == '-':
                num_total += num * sign
                sign = 1 if c == '+' else -1
                num = 0
            elif c == 'x':
                coff_total += num * sign
                num,sign = 0,1
            else:
                num = num * 10 + int(c)

        if num != 0:
            num_total += num * sign

        return [num_total, coff_total]
