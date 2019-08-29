# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:   
    def longestConsecutive(self, root: TreeNode) -> int:
        # https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/
        if root is None:
            return 0
        queue = [(root, 1)]
        max_path_length  = 0
        while queue:
            node, path_length = queue.pop()
            max_path_length = max(path_length, max_path_length)
            if node.left:
                if node.left.val == node.val + 1:
                    queue.append((node.left, path_length+1))
                else:
                    queue.append((node.left, 1))
            if node.right:
                if node.right.val == node.val + 1:
                    queue.append((node.right, path_length+1))
                else:
                    queue.append((node.right, 1))
        return max_path_length