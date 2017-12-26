import itertools
import random
class Solution(object):
   """
   https://leetcode.com/problems/shuffle-an-array/#/description
   """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums



    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        def anagram(nums):
            return list(itertools.permutations(list(nums)))
        returnList=anagram(self.nums)
        return list(returnList[random.randint(0,len(returnList)-1)])



# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3,4])
param_1 = obj.reset()
param_2 = obj.shuffle()
