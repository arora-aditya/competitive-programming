def nextGreaterElements(nums):
    """
    https://leetcode.com/problems/next-greater-element-ii/#/description
    :type nums: List[int]
    :rtype: List[int]
    """
    def returnNumber(num,nums):
        i=nums.index(num)+1
        index=i-1
        while i <= len(nums) and i != index:
            if i == len(nums):
                i=0
            if nums[i] > num:
                return nums[i]
            i += 1
        return -1
    returnList=[]
    sorted_nums=sorted(nums)
    for num in nums:
        returnList.append(returnNumber(num,nums))
    return returnList
print(nextGreaterElements([5,4,3,2,1]))
