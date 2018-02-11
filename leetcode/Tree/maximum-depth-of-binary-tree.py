# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        ans, level = 0, [root]
        while level:
            ans += 1
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [node for node in temp if node]
        return ans
            
