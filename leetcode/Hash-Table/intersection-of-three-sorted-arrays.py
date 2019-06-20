class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # https://leetcode.com/problems/intersection-of-three-sorted-arrays/
        return list(sorted(set(arr1) & set(arr2) & set(arr3)))