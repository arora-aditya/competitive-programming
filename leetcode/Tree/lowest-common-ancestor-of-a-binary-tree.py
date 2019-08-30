# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
        if root is None:
            return None
        if root == p or root == q:
            # print('O', root.val, p.val, q.val)
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left is not None and right is None:
            # print('L', left.val, p.val, q.val)
            return left
        elif right is not None and left is None: 
            # print('R', right.val, p.val, q.val)
            return right
        elif left is not None and right is not None:
            return root
        