class RandomizedSet(object):
    """
    https://leetcode.com/problems/insert-delete-getrandom-o1/description/
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.se = set()
        self.le = 0


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """

        if val in self.se:
            return False
        self.se = self.se | set([val])
        self.le += 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.se:
            return False
        self.se = self.se - set([val])
        self.le -= 1
        return True


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return list(self.se)[random.randint(0,self.le-1)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
