# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderTraversal_countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        counter = 1
        level = [root]
        while level:
            temp = []
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level = temp
            counter += len(level)
        return counter

    def countNodes(self, root):
        # 1. If left sub tree height equals right sub tree height then,
        #     a. left sub tree is perfect binary tree
        #     b. right sub tree is complete binary tree
        # 2. If left sub tree height greater than right sub tree height then,
        #     a. left sub tree is complete binary tree
        #     b. right sub tree is perfect binary tree
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

        def getDepth(self, root):
            if not root:
                return 0
            return 1 + self.getDepth(root.left)
