# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node):
        if not node:
            return -1
        i = max(self.dfs(node.left), self.dfs(node.right)) + 1
        if i >= len(self.res):
            self.res.append([])
        self.res[i].append(node.val)
        return i
    def findLeaves(self, root):
        """
        https://leetcode.com/problems/find-leaves-of-binary-tree/description/
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(root)
        return self.res
        
