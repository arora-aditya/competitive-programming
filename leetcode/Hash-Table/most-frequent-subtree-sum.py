# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        https://leetcode.com/problems/most-frequent-subtree-sum/description/
        :type root: TreeNode
        :rtype: List[int]
        """
        di = {}
        def recurse(root):
            if root == None: return 0
            su = root.val + recurse(root.left) + recurse(root.right)
            if su not in di:
                di[su] = 0
            di[su] += 1
            return su
        recurse(root)
        re, ma = [], 0
        for i in di:
            if di[i] > ma:
                re = [i]
                ma = di[i]
            elif di[i] == ma:
                re.append(i)
        return re
