class Solution:
    def levelOrderBottom(self, root):
        """
        https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
            # print(ans, temp, level)
        return ans[::-1]
