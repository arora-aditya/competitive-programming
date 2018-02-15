class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        exist = {x: i for i, x in enumerate(list1)}
        tmp = float('inf')
        ans = []

        for i, x in enumerate(list2):
            if x in exist:
                if i + exist[x] < tmp:
                    tmp = i + exist[x]
                    ans = [x]
                elif i + exist[x] == tmp:
                    ans.append(x)

        return ans
