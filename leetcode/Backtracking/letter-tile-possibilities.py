class Solution: 
    def numTilePossibilities(self, tiles: str) -> int:
        # https://leetcode.com/problems/letter-tile-possibilities/
        ans = 0
        for i in range(1,len(tiles)+1):
            ans += len(set(itertools.permutations(tiles,i)))
        return ans