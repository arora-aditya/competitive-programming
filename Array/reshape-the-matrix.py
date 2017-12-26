class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        https://leetcode.com/problems/reshape-the-matrix/description/
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        new_matrix=[]
        list_of_numbers=[]
        count=0
        if r*c==len(nums)*len(nums[0]):
            for i in range(len(nums)):
                for j in range(len(nums[i])):
                    list_of_numbers.append(nums[i][j])
            for i in range(r):
                row=[]
                for j in range(c):
                    row.append(list_of_numbers[count])
                    count+=1
                new_matrix.append(row)
            return (new_matrix)
        else:
             return (nums)
