# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        https://leetcode.com/problems/find-bottom-left-tree-value/description/
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
            # print(ans, temp, level)
        return ans[-1][0]
