class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        # https://leetcode.com/problems/delete-columns-to-make-sorted/
        B = list(map(list,zip(*A)))
        answerCount = 0
        for i in range(len(B)):
            if B[i] != sorted(B[i]):
                answerCount+=1
        return answerCount
    def slowerString_minDeletionSize(self, A: List[str]) -> int:
        counter = 0
        for j in range(len(A[0])):
            prev = A[0][j]
            for i in range(1, len(A)):
                if A[i][j] < prev:
                    counter += 1
                    break
                prev = A[i][j]
        return counter
