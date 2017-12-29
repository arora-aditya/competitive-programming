def singleNumber(nums):
    """
    https://leetcode.com/problems/single-number-iii/#/description
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
        return_list = []
        for num in nums_dict:
            if nums_dict[num] == 1:
                return_list.append(num)
        return return_list

print(singleNumber([1, 2, 1, 3, 2, 5]))
