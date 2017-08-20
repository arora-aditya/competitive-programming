class Solution(object):
    def maxArea(self, height):
        """
        https://leetcode.com/problems/container-with-most-water/description/
        :type height: List[int]
        :rtype: int
        """
        max_area = area = 0
        left, right = 0, len(height) - 1
        while left < right:
            l, r = height[left], height[right]
            if l < r:
                area = (right - left) * l
                while height[left] <= l:
                    left += 1
            else:
                area = (right - left) * r
                while height[right] <= r and right:
                    right -= 1
            if area > max_area:
                max_area = area
        return max_area
