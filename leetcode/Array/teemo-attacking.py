class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        https://leetcode.com/problems/teemo-attacking/description/
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        intervals = []
        for i in timeSeries:
            intervals.append([i,i+duration])
        out = []
        for i in sorted(intervals, key=lambda i: i[0]):
            if out and i[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out += i,
        cnt = 0
        for i in out:
            cnt += i[1] - i[0]
        return cnt
