count=0
def moveZeroes(nums):
    """
    https://leetcode.com/problems/
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    length=len(nums)+1
    def isZero(num,length=length):
        global count
        if num==0:
            return length
        count +=1
        return count
    nums.sort(key=isZero)
    print(nums)

moveZeroes([0, 1])
