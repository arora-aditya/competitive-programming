class Solution:
    def compress(self, chars: List[str]) -> int:
        # https://leetcode.com/problems/string-compression/submissions/
        i, j= 0, 0
        while i < len(chars):
            char = chars[i]
            chars[j] = char
            j += 1
            # capture the multiple numbers
            count = 1
            while i+1 < len(chars) and char == chars[i+1]:
                i += 1
                count += 1
            if count > 1:
                for num in str(count):
                    chars[j] = num
                    j += 1
            i += 1
        return j