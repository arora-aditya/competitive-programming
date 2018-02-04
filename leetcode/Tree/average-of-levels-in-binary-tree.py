class Solution:
    def averageOfLevels(self, root):
        """
        https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
        :type root: TreeNode
        :rtype: List[float]
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
        k = []
        for i in ans:
            k.append(sum(i)/len(i))
        return k
