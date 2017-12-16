class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        l1 = set(list1)
        l2 = set(list2)
        l = l1 & l2
        # print(l)
        save = []
        mi = len(list1) + len(list2)
        if len(l) == 0:
            return list(l)[0]   
        for i in (l):
            # print(save)
            k = list1.index(i) + list2.index(i)
            # print(i,k)
            if k < mi:
                mi = k
                del save[:]
                save = [i]         
            elif k == mi:
                save.append(i)
        return save
            
