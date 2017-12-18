class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        https://leetcode.com/problems/valid-square/description/
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def dist(l1,l2):
            return pow(pow(l1[0]-l2[0],2)+pow(l1[1]-l2[1],2),0.5)
        def slope(l1,l2):
            # print(l1,l2,float(l2[1] - l1[1])/float(l2[0] - l1[0]))
            if (l2[0] - l1[0]) == 0:
                # print(float('inf'))
                return float('inf')
            # print((l2[1] - l1[1])/(l2[0] - l1[0]))
            return float(l2[1] - l1[1])/float(l2[0] - l1[0])
        def isPerp(l1,l2,l3):
            print((l1,l2),slope(l1,l2),slope(l2,l3), slope(l1,l2) * slope(l2,l3), slope(l1,l2) * slope(l2,l3)==-1)
            if slope(l1,l2) == 0 and slope(l2,l3) == float('inf'):
                return True
            if slope(l1,l2) * slope(l2,l3) <= -0.99 and slope(l1,l2) * slope(l2,l3) >= -1.01:
                return True
            return False
          
        if (dist(p1,p2) == dist(p2,p3) and dist(p2,p3) == dist(p3,p4) and dist(p3,p4) == dist(p1,p2)) or (dist(p1,p3) == dist(p3,p2) and dist(p3,p2) == dist(p2,p4) and dist(p2,p4) == dist(p1,p3)) or (dist(p1,p3) == dist(p3,p4) and dist(p3,p4) == dist(p4,p2) and dist(p4,p2) == dist(p1,p3)):
            if isPerp(p1,p2,p3) or isPerp(p1,p2,p4) or isPerp(p1,p3,p2) or isPerp(p1,p3,p4) or isPerp(p1,p4,p2) or isPerp(p1,p4,p3):
                return True
        return False
