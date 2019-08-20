# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder(self, root: TreeNode) -> List[int]:
        # https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
        if root.left:
            self.inorder(root.left)
        self.ans.append(root.val)
        if root.right:
            self.inorder(root.right)
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.ans = []
        if root1:
            self.inorder(root1)
        r1 = self.ans
        self.ans = []
        if root2:   
            self.inorder(root2)
        r2 = self.ans
        return sorted(r1 + r2)