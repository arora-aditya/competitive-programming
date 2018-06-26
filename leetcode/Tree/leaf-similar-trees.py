# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateLeafSequence(self, root):
        """
        https://leetcode.com/problems/leaf-similar-trees/description/
        :type root: TreeNode
        :rtype: List[int]
        """
        l1 = []
        st = []
        while root or st:
            while root:
                st.append(root)
                root = root.left

            top = st.pop()
            if not top.left and not top.right:
                l1.append(top.val)
            root = top.right
        return l1
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.generateLeafSequence(root1) == self.generateLeafSequence(root2)
        
