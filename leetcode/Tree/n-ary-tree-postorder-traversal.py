"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        stack = [root]

        while stack:
            top = stack[-1]
            if top is None:
                stack.pop()
                continue
            if not top.children:
                res.append(top.val)
                stack.pop()
                continue

            stack.append(top.children.pop(0))

        return res

    def recursive_N_ary_postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        for child in root.children:
            ans.extend(self.postorder(child))
        ans.append(root.val)
        return ans
