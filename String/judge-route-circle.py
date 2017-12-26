class Solution(object):
    def judgeCircle(self, moves):
        """
        https://leetcode.com/problems/judge-route-circle/description/
        :type moves: str
        :rtype: bool
        """
        ud , lr = 0, 0
        for char in moves:
            if char == "U":
                ud += 1
            elif char == "D":
                ud -= 1
            if char == "R":
                lr += 1
            elif char == "L":
                lr -= 1
        return ud == 0 and lr == 0
