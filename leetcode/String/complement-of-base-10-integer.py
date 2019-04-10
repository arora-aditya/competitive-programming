class Solution:
    def bitwiseComplement(self, N: int) -> int:
        # https://leetcode.com/problems/complement-of-base-10-integer/
        bi = bin(N)[2:]
        bi = bi.replace('0','2')
        bi = bi.replace('1','0')
        bi = bi.replace('2','1')
        return int('0b'+bi, 2)
