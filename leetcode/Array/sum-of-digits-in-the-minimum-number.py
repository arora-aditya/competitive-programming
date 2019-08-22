class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        # https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/
        mi = min(A)
        su = sum(map(int, list(str(mi))))
        return (su + 1) % 2 