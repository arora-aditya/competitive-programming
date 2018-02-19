# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        https://leetcode.com/problems/binary-tree-preorder-traversal/description/
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if root:
            res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)
