class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # https://leetcode.com/problems/diagonal-traverse/
        if matrix == []:
            return []
        di = {}
        suList = []
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            # print(matrix[i])
            for j in range(c):
                if i+j in di:
                    di[i+j].append(matrix[i][j])
                else:
                    di[i+j] = [matrix[i][j]]
        ans = []
        for k in range(r+c-1):
            if k%2 == 0:
                ans.extend(di[k][::-1])
            else:
                ans.extend(di[k])
        return ans