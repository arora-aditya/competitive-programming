class Solution:
    def selfDividingNumbers(self, left, right):
        """
        https://leetcode.com/problems/self-dividing-numbers/description/
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l = []
        def isSelfDividing(num):
            numAsList = list(str(num))
            for i in numAsList:
                if i == '0' or int(num)%int(i) != 0: 
                    return False       
            return True
        for i in range(left,right+1):
            if isSelfDividing(i):
                l.append(i)
        return l
