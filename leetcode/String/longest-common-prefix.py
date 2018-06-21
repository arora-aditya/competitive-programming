class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(zip(*A))
    def longestCommonPrefix(self, strs):
        """
        https://leetcode.com/problems/longest-common-prefix/description/
        :type strs: List[str]
        :rtype: str
        """
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
