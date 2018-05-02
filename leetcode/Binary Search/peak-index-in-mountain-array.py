class Solution:
    def peakIndexInMountainArray(self, A):
        """
        https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
        :type A: List[int]
        :rtype: int
        """
        low, high = 0, len(A)-1
        peak = 0

        while low <= high:
            mid = low + (high-low)//2
            if A[mid-1] < A[mid] > A[mid+1]:
                peak = mid
                return peak
            elif A[mid-1] < A[mid]:
                low = mid+1
            else:
                high = mid-1
