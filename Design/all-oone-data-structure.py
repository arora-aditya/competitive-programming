class AllOne(object):

    def __init__(self):
        """
        https://leetcode.com/problems/all-oone-data-structure/description/
        Initialize your data structure here.
        """
        self.di = {}



    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        self.di[key] = self.di.get(key,0) + 1
        print(self.di)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if self.di.get(key,-1) != -1:
            if self.di[key] == 1:
                def removekey(d, key):
                    r = dict(d)
                    del r[key]
                    return r
                self.di = removekey(self.di, key)
            else:
                self.di[key]-=1
        print(self.di, key)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        try:
            ma = max(self.di.values())
        except ValueError:
            return ""
        for key in self.di:
            if self.di[key] == ma:
                return key


    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        try:
            mi = min(self.di.values())
        except ValueError:
            return ""
        # print(mi)
        for key in self.di:
            if self.di[key] == mi:
                # print(key)
                return key



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

# runtime: 298ms
# test cases passed: 15/15
