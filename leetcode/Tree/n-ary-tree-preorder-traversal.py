"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from typing import List
class Solution:
    # https://leetcode.com/problems/n-ary-tree-preorder-traversal/
    def preorder(self, root: 'Node') -> List[int]:
        ret, q = [], root and [root]
        while q:
            node = q.pop()
            ret.append(node.val)
            q += [child for child in reversed(node.children)]
        return ret
    def recursive_N_ary_preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = [root.val]
        for child in root.children:
            ans.extend(self.preorder(child))
        return ans
