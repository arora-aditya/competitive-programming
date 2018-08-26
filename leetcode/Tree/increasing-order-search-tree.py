# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        https://leetcode.com/problems/binary-tree-inorder-traversal/description/
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        l = self.inorderTraversal(root)
        rootCopy = TreeNode(l[0])
        traverse = rootCopy
        for i in l[1:]:
            traverse.left = None
            traverse.right = TreeNode(i)
            traverse = traverse.right
        return rootCopy
        
