def singleNumber(nums):
    """
    https://leetcode.com/problems/single-number/#/description
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    print(nums)
    print(set(nums))
    for i,num in enumerate(sorted(set(nums))):
        try:
            print(i,num,(i*2)+1)
            if nums[(i*2)+1] != num:
                break
        except:
            True
    return num
