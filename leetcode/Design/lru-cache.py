class LRUCache(object):
    """
    https://leetcode.com/problems/lru-cache/description/
    """
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity
        self.data = {}
        self.stack = []


    def get(self, key):
        # print("get", key, "->", self.data, self.stack)
        """
        :type key: int
        :rtype: int
        """
        if key in self.data:
            self.stack.remove(key)
            self.stack.insert(0, key)
            return self.data[key]
        else:
            return -1


    def put(self, key, value):
        # print("put", key, value, "->", self.data, self.stack)
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.data:
            self.stack.remove(key)
            self.stack.insert(0, key)
            self.data[key] = value
        elif len(self.data) >= self._capacity:
            self.data.pop(self.stack.pop(), None)
            self.stack.insert(0, key)
            self.data[key] = value
        else:
            self.stack.insert(0, key)
            self.data[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
