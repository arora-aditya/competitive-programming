# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
        self.a = 0
        self.inorder(root)
        return root
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.right)
        root.val += self.a
        self.a = root.val
        self.inorder(root.left)