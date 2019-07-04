class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return list(zip(*A))
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # https://leetcode.com/problems/longest-common-prefix/description/
        if strs == []:
            return ""
        l = []
        for i in strs:
            l.append(list(i))
        l = self.transpose(l)
        cnt = 0
        for i in map(lambda x: len(set(x)), l):
            if i == 1:
                cnt += 1
            else:
                break
        return strs[0][:cnt]