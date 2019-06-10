class Solution:
    def removeVowels(self, S: str) -> str:
        # https://leetcode.com/problems/remove-vowels-from-a-string/
        se = set(['a','e','i','o','u'])
        ans = ''
        for s in S:
            if s not in se:
                ans += s
        return ans