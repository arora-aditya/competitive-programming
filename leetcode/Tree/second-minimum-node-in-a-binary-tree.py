# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.extend([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
            # print(ans, temp, level)
        try:
            return sorted(set(ans))[1]
        except:
            return -1
