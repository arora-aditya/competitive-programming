class Solution(object):
    def kthSmallest(self, root, k):
        """
        https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
        :type root: TreeNode
        :type k: int
        :rtype: int
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
        li = []
        for i in ans:
            li.extend(i)
        # print(sorted(li))
        return sorted(li)[k-1]
        
