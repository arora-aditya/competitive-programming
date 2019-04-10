class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        # https://leetcode.com/problems/find-and-replace-in-string/
        S = list(S)
        for i, x, y in sorted(zip(indexes, sources, targets), reverse = True):
            if all(i+k < len(S) and S[i+k] == x[k] for k in range(len(x))):
                S[i:i+len(x)] = list(y)
        return "".join(S)

    def failed_findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        new_indexes = []
        for i in range(len(indexes)):
            flag = True
            for j in range(len(sources[i])):
                print(S[indexes[i]+j], sources[i][j], i, j)
                if S[indexes[i]+j] != sources[i][j]:
                    flag = False
            if flag:
                new_indexes.append(i)
        print(new_indexes)
        le = 0
        for i in sorted(new_indexes):
            print(S, le)
            S = S[:i + le] + re.sub(sources[i], targets[i], S[i+le:], 1)
            le += len(targets[i]) - len(sources[i])
        return S
