def findDuplicates(nums):
    """
    https://leetcode.com/problems/find-all-duplicates-in-an-array/#/description
    :type nums: List[int]
    :rtype: List[int]
    """
    def duplicate(x,pos,a=nums):
        if x in a[:pos]:
            return x
    return list(set(map(duplicate,nums,range(len(nums)))))[1:]
    
print(findDuplicates([4,3,2,7,8,2,3,1]))
