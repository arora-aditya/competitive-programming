def containsNearbyDuplicate(nums, k):
    """
    https://leetcode.com/problems/contains-duplicate-ii/#/description
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    dic = {}
    for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    return False
