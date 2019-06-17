class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        # https://leetcode.com/problems/airplane-seat-assignment-probability
        return 1.0 if n == 1 else 0.5