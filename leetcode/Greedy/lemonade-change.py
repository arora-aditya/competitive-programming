class Solution:
    def lemonadeChange(self, bills):
        """
        https://leetcode.com/problems/lemonade-change/description/
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0
        twenty = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                ten += 1
                five -= 1
            elif bill == 20:
                if five >= 1 and ten >= 1:
                    twenty += 1
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    twenty += 1
                    five -= 3
                else:
                    return False
        return True
