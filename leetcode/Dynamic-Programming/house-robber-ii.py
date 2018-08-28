class Solution(object):
    def rob(self, nums):
        """
        https://leetcode.com/problems/house-robber-ii/description/
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
            return max(nums[0], nums[1], nums[2])
        if lea == 4:
            return max(nums[1] + nums[3], nums[0] + nums[2])
        dpl = [0] * lea
        dpl[0], dpl[1], dpl[2], dpl[3] = nums[0], nums[1], nums[0] + nums[2], nums[3] + nums[0]
        dpr = [0] * lea
        dpr[0], dpr[1], dpr[2], dpr[3] = nums[0], nums[1], nums[2], nums[3] + nums[1]
        for i in range(4, lea-1):
            dpl[i] = nums[i] + max(dpl[i-2], dpl[i-3])
            dpr[i] = nums[i] + max(dpr[i-2], dpr[i-3])
        dpr[-1] = nums[-1] + max(dpr[-4], dpr[-3])
        return max(dpl[-2], dpl[-3], dpr[-1], dpr[-2])
