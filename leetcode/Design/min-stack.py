class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mi = 0
        self.li = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.li.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.li.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.li[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.li)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
