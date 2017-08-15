def productExceptSelf(nums):
    """
    https://leetcode.com/problems/product-of-array-except-self/#/description
    :type nums: List[int]
    :rtype: List[int]
    """
    product=1
    for num in nums:
        if num==0:
            product=0
            break
        product=product*num
    if product==0:
        return [0]*len(nums)
    return [int(product/x) for x in nums]
