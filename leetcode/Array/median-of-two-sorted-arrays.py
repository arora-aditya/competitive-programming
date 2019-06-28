class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        l = len(nums1)
        if l%2==1:
            return nums1[l//2]
        return (nums1[l//2]+nums1[l//2-1])/2