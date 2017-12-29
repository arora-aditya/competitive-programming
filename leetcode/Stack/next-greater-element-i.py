def nextGreaterElement(findNums, nums):
    """
    https://leetcode.com/problems/next-greater-element-i/#/description
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    returnList=[]
    for num in findNums:
        flag=True
        index=nums.index(num)
        for i in range(index,len(nums)):
            if nums[i] > num:
                returnList.append(nums[i])
                flag=False
                break
        if flag:
            returnList.append(-1)
    return returnList

print(nextGreaterElement([4,1,2],[1,3,4,2]))
