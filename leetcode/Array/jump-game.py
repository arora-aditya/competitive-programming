class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # started from the back
        if len(nums) < 2:
            return True

        min_successful_index = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= min_successful_index:
                min_successful_index = i

        return min_successful_index == 0

    def dp_canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums[0] == 0:
            if len(nums) != 1:
                return False
            else:
                return True

        dp = [-1]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]-1, nums[i])
            if dp[i] == 0:
                break
        print(dp)
        return dp[-1] != -1
