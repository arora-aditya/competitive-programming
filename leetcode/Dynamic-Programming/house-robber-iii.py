# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.helper(root))

    def helper(self, root):
        if root == None:
            return [0,0]
        if root.left == None and root.right == None:
            return [0, root.val]
        left = self.helper(root.left)
        right = self.helper(root.right)
        return [max(left) + max(right), root.val + left[0] + right[0]]
