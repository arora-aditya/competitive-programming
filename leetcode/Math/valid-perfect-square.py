class Solution:
    def isPerfectSquare(self, x):
        """
        https://leetcode.com/problems/valid-perfect-square/description/
        :type num: int
        :rtype: bool
        """
        def check(li, num):
            for i in li[-5:]:
                if i != int(num):
                    return False
            return True
        li = [None, None, None, None, None, None]
        root = 1
        flag = True
        while True:
            root = 0.5 * (root + (x/root))
            # print(root, check(li, root), li[-5:])
            if check(li, root):
                return int(root) == root
            li.append(int(root))
