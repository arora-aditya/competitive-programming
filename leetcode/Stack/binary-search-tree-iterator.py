# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # https://leetcode.com/problems/binary-search-tree-iterator/
    def __init__(self, root: TreeNode):
        
        self.stack = []
        self.leftmost_inorder(root)
        
    def leftmost_inorder(self, root):
        
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        
        topmost_node = self.stack.pop()
        
        if topmost_node.right:
            self.leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0