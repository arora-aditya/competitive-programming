from collections import defaultdict
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if len(set(target) - set(source)) > 0:
            return -1
        di = defaultdict(list)
        for i in range(len(source)):
            di[source[i]].append(i)
        i = 0
        ans = 0
        while i < len(target):
            start_index = di[target[i]][0]
            if i < len(target) - 1:
                next_index = list(filter(lambda x: x > start_index, di[target[i+1]]))
            else:
                ans += 1
                break
            # print(i, start_index, next_index)
            while len(next_index) > 0:
                start_index = next_index[0]
                # print(i, start_index, next_index)
                i += 1
                if i < len(target) - 1:
                    next_index = list(filter(lambda x: x > start_index, di[target[i+1]]))
                else:
                    break
                # print(len(next_index))
            ans += 1
            # print(i, ans, target[i], target[i-1])
            i += 1
        print(i, len(target), start_index, next_index)
        return ans    
            
S = Solution()

testcases = [
    dict(source = "abc", target = "abcbc"),
    dict(source = "abc", target = "acdbc"),
    dict(source = "xyz", target = "xzyxz"),
    dict(source = "abc", target = "ab"*1000),
    dict(source = "bxdisnclwdrpcqamhqqvudgtdbsdikhzzbnlgzlspozvhdkunxkpevnqvyrfowanagolpwvezuvnhgxvjopcvrkdaippmwgkofbo", target="ntzebqmlrzxissncdlvcxbojgbnnphtfdunjpzroegfdvieaajafjkidpxbrgsjpgmalekhjckwgygfz")
]

for testcase in testcases:
    print(f"{testcase}: {S.shortestWay(**testcase)}")