# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        # https://leetcode.com/problems/univalued-binary-tree
        bo = True
        val = root.val
        level = [root]
        while level:
            temp = []
            for node in level:
                if node.val != val:
                    return False
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level = temp
        return True
