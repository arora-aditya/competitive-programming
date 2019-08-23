class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # https://leetcode.com/problems/unique-number-of-occurrences/
        di = {}
        for num in arr:
            di[num] = di.get(num, 0) + 1
        v = di.values()
        return len(set(v)) == len(v)