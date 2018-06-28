class Logger:

    def __init__(self):
        """
        https://leetcode.com/problems/logger-rate-limiter/description/
        Initialize your data structure here.
        """
        self.a = {}


    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.a:
            self.a[message] = timestamp
            return True
        else:
            if timestamp - self.a[message] >= 10:
                self.a[message] = timestamp
                return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
