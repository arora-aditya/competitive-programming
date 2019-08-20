class Solution:
    def sumZero(self, n: int) -> List[int]:
        # https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
        L, rem = n // 2, n % 2
        if rem != 0: ans = [0]
        else: ans = []
        for i in range(1,L+1):
            ans.append(-i)
            ans.append(i) 
        return ans