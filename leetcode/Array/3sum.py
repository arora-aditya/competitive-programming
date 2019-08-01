class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # https://leetcode.com/problems/3sum/
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            j = i + 1
            # small optimization
            if nums[i] + nums[j] + nums[j + 1] > 0:
                return res
            k = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                else:
                    if total == 0:
                        res.append([nums[i], nums[j], nums[k]])
                    j += 1
        return res