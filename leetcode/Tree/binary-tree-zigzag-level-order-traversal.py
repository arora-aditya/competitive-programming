class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
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
        for i in range(len(ans)):
            if i%2 == 1:
                ans[i] = ans[i][::-1]
        return ans
