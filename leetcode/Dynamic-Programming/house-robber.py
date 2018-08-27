class Solution(object):
    def rob(self, nums):
        """
        https://leetcode.com/problems/house-robber/description/
        :type nums: List[int]
        :rtype: int
        """
        lea = len(nums)
        if lea == 0:
            return 0
        if lea == 1:
            return nums[0]
        if lea == 2:
            return max(nums)
        if lea == 3:
            return max(nums[0] + nums[2], nums[1])
        dp = [0] * lea
        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[0] + nums[2]
        for i in range(3, lea):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])
        return max(dp[-1], dp[-2])
