class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # https://leetcode.com/problems/high-five/
        di = {}
        for i, score in items:
            di[i] = di.get(i, []) + [score] 
        ans = []
        for i, scores in di.items():
            top5 = list(sorted(scores, reverse=True))[:5]
            # print(i, top5, scores)
            ans.append([i, sum(top5)//5])
        return sorted(ans, key=lambda x: x[0])