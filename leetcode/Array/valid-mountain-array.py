class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        # https://leetcode.com/problems/valid-mountain-array/
        if len(A) < 3:
            return False
        flag = True
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                return False
            if flag:
                if not (A[i] > A[i-1]):
                    if i == 1:
                        return False
                    flag = False
            else:
                if not (A[i] < A[i-1]):
                    return False
        return True and not flag
