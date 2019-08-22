class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # https://leetcode.com/problems/find-smallest-common-element-in-all-rows/
        mat = list(map(set, mat))
        ans = mat[0]
        for row in mat:
            ans &= row
        # print(ans)
        return min(ans) if ans else -1