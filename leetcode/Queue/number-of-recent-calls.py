from collections import deque
class RecentCounter(object):
    # https://leetcode.com/problems/number-of-recent-calls/
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        self.q.append(t)
        while len(self.q)>0 and self.q[0]<t-3000:
            self.q.popleft()

        return len(self.q)

    # Same approach but using strings without pop left
    def failed__init__(self):
        self.arr = []

    def failed_ping(self, t: int) -> int:
        counter = 0
        i = -1
        for i in range(len(self.arr)-1,-1,-1):
            if self.arr[i] < t - 3000:
                break
            counter += 1
        # print(counter, self.arr)
        self.arr = self.arr[-counter:]
        self.arr.append(t)
        return counter + 1


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
