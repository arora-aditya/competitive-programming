class Solution:
    def reverseVowels(self, s: str) -> str:
        # https://leetcode.com/problems/reverse-vowels-of-a-string/
        vowels = set(['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U'])
        s = list(s)
        front, back = 0, len(s) - 1
        while front < back:
            # print(front, back, s[front], s[back])
            if s[front] in vowels and s[back] in vowels:
                s[back], s[front] = s[front], s[back]
                front+=1
                back-=1 
            if s[back] not in vowels:
                back-=1 
            if s[front] not in vowels:
                front+=1
        return ''.join(s)