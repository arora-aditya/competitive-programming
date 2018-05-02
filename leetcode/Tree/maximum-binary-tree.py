class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        https://leetcode.com/problems/maximum-binary-tree/description/
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        max_n = max(nums)
        max_i = nums.index(max_n)
        lnums = nums[:max_i]
        rnums = nums[max_i+1:]
        node = TreeNode(max_n)
        node.left = self.constructMaximumBinaryTree(lnums)
        node.right = self.constructMaximumBinaryTree(rnums)
        return node
