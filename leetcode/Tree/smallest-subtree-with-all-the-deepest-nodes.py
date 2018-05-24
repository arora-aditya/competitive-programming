import numpy as np

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def transpose(self, A):
        """
        https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return np.array(A).transpose().tolist()

    def getAllParents(self, root, ma):
        ans = []
        st = [root]
        while True:
            if root != "1":
                st.append(ma[root])
                root = ma[root]
            else:
                break
        return st
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return []
        ans, level = [], [root]
        ma = {root:"1"}
        while level:
            ans.append(level)
            temp = []
            for node in level:
                ma[node.left] = node
                ma[node.right] = node
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        helper = []
        # print(ans, [[a.val for a in x] for x in ans])
        # print(ma)
        for i in ans[-1]:
            helper.append(self.getAllParents(i, ma))
            # print(helper[-1])
        helper = self.transpose(helper)
        # print(helper)
        for i in helper:
            se = set(i)
            le = len(set(i))
            if le == 1:
                return list(se)[0]
        # print(helper)
        # print(ans,[[a.val for a in x] for x in ans])
