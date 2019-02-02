class Solution(object):
    def searchRange(self, nums, target):
        """
        https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []: return [-1, -1]
        flag = False
        le = len(nums)
        low, high = 0, le - 1
        if low == high and nums[low] == target: return [low, high]
        while low <= high:
            mid = int(0.5 * (low + high))
            print(low, mid, high)
            if nums[mid] == target:
                flag = True
                break
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        # print(flag)
        if flag:
            low = mid
            high = mid
            while low > 1 and nums[low-1] == target:
                low -= 1
            while high + 1 < le and nums[high+1] == target:
                high += 1
            return [low, high]
        else:
            return [-1, -1]

S = Solution()
print(S.searchRange([1, 4], 4))
