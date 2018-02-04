class Solution(object):
    def twoSum(self, nums, target):
        """
        https://leetcode.com/problems/two-sum/description/
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        di = collections.defaultdict(list)
        for i in range(len(nums)):
            if(nums[i] in di):
                return [di[nums[i]][0], i]
            di[target - nums[i]] = di[target - nums[i]]
            di[target - nums[i]].append(i)
        print(di)
