from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # https://leetcode.com/problems/bulls-and-cows/
        ses, seg = Counter(secret), Counter(guess)
        ik = ses & seg
        C = 0
        for k in ik:
            C += ik[k]
        B = 0 
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                B += 1
                C -= 1
        return f"{B}A{C}B"