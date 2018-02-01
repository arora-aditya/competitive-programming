class Solution:
    def numJewelsInStones(self, J, S):
        """
        https://leetcode.com/problems/jewels-and-stones/description/
        :type J: str
        :type S: str
        :rtype: int
        """
        J = set(J)
        cnt = 0
        for i in S:
            if i in J:
                cnt += 1
        return cnt
