# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        # https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
        if not root:
            return []
        _ans, level = [], [root]
        while level:
            _ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        ans = -1
        ma = -float('inf')
        _ans = list(map(sum, _ans))
        # print(_ans)
        for i, x in enumerate(_ans):
            if x > ma:
                ans = i
                ma = x
        return ans + 1