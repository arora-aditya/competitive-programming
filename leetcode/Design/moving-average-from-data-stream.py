class MovingAverage:
    """
    https://leetcode.com/problems/moving-average-from-data-stream/description/
    """
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.li = []
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.li.append(val)
        return sum(self.li[-self.size:])/len(self.li[-self.size:])


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
