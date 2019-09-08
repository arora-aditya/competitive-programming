class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # https://leetcode.com/problems/search-a-2d-matrix/
        targetRow = []
        for row in matrix:
            if not row: return False
            if row[-1] >= target:
                targetRow = row
                break
        if not targetRow: return False
        left = 0
        right = len(targetRow) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if targetRow[mid] == target:
                return True
            elif targetRow[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False