class Solution:
    letters = [None, None, ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

    def letterCombinations(self, digits: str) -> List[str]:
        # https://leetcode.com/problems/letter-combinations-of-a-phone-number
        if not digits: return []
        pre = Solution.letterCombinations(None, digits[:-1])
        if pre == []: pre = [""]
        return [x + y for x in pre for y in Solution.letters[int(digits[-1])]]