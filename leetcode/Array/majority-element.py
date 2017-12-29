import operator
def majorityElement(nums):
    """
    https://leetcode.com/problems/majority-element/#/description
    :type nums: List[int]
    :rtype: int
    """
    num_dict = {k: nums.count(k) for k in set(nums)}
    count=0
    key_save=0
    for key in num_dict:
        if num_dict[key] > count:
            count=num_dict[key]
            key_save=key
    return key_save
