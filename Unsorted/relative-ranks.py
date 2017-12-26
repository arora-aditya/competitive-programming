def findRelativeRanks(nums):
    """
    https://leetcode.com/problems/relative-ranks/#/description
    :type nums: List[int]
    :rtype: List[str]
    """
    return_list = nums[:]
    nums.sort(reverse = True)
    return_list[return_list.index(nums[0])], return_list[return_list.index(nums[1])], return_list[return_list.index(nums[2])] = "Gold Medal", "Silver Medal", "Bronze Medal"
    
    for i in range(len(nums)-3):
        return_list[return_list.index(nums[i+3])] = str(i+4)
    return return_list

print(findRelativeRanks([5, 4, 3, 2, 1]))
