class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        https://leetcode.com/problems/partition-labels/description/
        """
        # print(len(S))
        dct = {}
        chars = []
        start = []
        end = []
        for i in range(len(S)-1,-1,-1):
            if S[i] not in dct:
                dct[S[i]]  = [i]
            else:
                dct[S[i]].append(i)
        l = sorted(dct, key = lambda k: dct[k][-1])
        for k in l:
            chars.append(k)
            end.append(dct[k][0])
            start.append(dct[k][-1])
        start.append(len(S))
        # print(chars)
        # print(start)
        # print(end)
        lk = []
        li = []
        for i in range(len(chars)):
            lk.append(start[i])
            lk.append(end[i])
            # print(lk, li)
            lk.sort()
            if lk[-1] < start[i+1]:
                li.append(lk[-1]-lk[0] + 1)
                lk.clear()
            lk.sort()
            # print(lk, li)
        assert(sum(li) == len(S))
        return li
