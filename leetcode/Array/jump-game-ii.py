class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://leetcode.com/problems/jump-game-ii/
        n, end, start, step = len(nums), 0, 0, 0
        while end < n-1:
            step += 1
            maxend = end + 1
            for i in range(start, end+1):
                if i + nums[i] >= n-1:
                    return step
                maxend=max(maxend, i+nums[i])
            start, end = end + 1, maxend
        return step
    def dp_jump(self, nums):
        # Time Limit Exceeded
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [i for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(min(len(nums),i+1+nums[i])-1, i, -1):
                print((i,j), dp)
                if dp[i] + 1 > dp[j]:
                    break
                dp[j] = min(dp[i] + 1, dp[j])
        return dp[-1]
