def singleNumber(nums):
    """
    https://leetcode.com/problems/single-number-ii/#/description
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return nums[0]
    else:
        nums.sort()
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num,0) + 1
        for num in nums_dict:
            if nums_dict[num] == 1:
                return num

print(singleNumber([0,1,1,1]))
