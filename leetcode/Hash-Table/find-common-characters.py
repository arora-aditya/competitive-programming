class Solution:
    def commonChars(self, arr: List[str]) -> List[str]:
        # https://leetcode.com/problems/find-common-characters/
        output = []
        for char in set(arr[0]):
            minCount = arr[0].count(char)
            for word in arr:
                count = word.count(char)
                minCount = min(minCount, count)
                if minCount == 0:
                    break
            for _ in range(minCount):
                output.append(char)
        return output
    def slower_solution_commonChars(self, A: List[str]) -> List[str]:
        # Less optimisations
        if not A:
            return []
        self.seen = set()

        dis = [self.word_to_dict(A[0])]
        for st in A[1:]:
            dis.append(self.word_to_dict(st, True))
        print(dis)
        se = set(list('qwertyuiopasdfghjklzxcvbnm'))
        for di in dis:
            se = se & di.keys()
        ret = []
        for char in se:
            mi = float('inf')
            for di in dis:
                mi = min(di[char], mi)
            ret += [char]*mi
        return ret
    def word_to_dict(self, st: str, check: bool = False) -> dict:
        di = {}
        for char in st:
            if not check:
                self.seen.add(char)
                di[char] = di.get(char, 0) + 1
            elif check and char in self.seen:
                di[char] = di.get(char, 0) + 1
        return di
