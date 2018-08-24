class MapSum(object):
    # https://leetcode.com/problems/map-sum-pairs/description/
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.di = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.di[key] = val


    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        count = 0
        for i in self.di:
            if i.startswith(prefix):
                count += self.di[i]
        return count



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
