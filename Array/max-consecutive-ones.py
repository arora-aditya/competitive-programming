def findMaxConsecutiveOnes(nums):
    """
    https://leetcode.com/problems/max-consecutive-ones/#/description
    :type nums: List[int]
    :rtype: int
    """
    maxLength=0
    j=-1
    zeroPlaces=[-1,len(nums)]
    for i in range(len(nums)+1):
        if i==len(nums) or nums[i] == 0:
            print(i,j,maxLength)
            maxLength=max(maxLength,i-j-1)
            j=i
    return maxLength
