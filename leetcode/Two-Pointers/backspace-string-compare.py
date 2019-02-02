class Solution:
    # https://leetcode.com/problems/backspace-string-compare/submissions/
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            while i >= 0 and (backS or S[i] == '#'):
                backS += 1 if S[i] == '#' else -1
                i -= 1
            while j >= 0 and (backT or T[j] == '#'):
                backT += 1 if T[j] == '#' else -1
                j -= 1
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i, j = i - 1, j - 1

    def stackApproach_backspaceCompare(self, S: str, T: str) -> bool:
        s,t = [], []
        for char in S:
            if char == '#':
                if s:
                    s.pop()
            else:
                s.append(char)
        for char in T:
            if char == '#':
                if t:
                    t.pop()
            else:
                t.append(char)
        return s == t
