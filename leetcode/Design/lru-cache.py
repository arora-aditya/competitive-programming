class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.current = 0
        self.start = Node(0, 0)
        self.end = Node(0, 0)
        self.start.next = self.end
        self.end.prev = self.start
        self.node_map = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.node_map:
            return -1
        
        node = self.node_map[key]
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = self.start.next
        node.next.prev = node
        self.start.next = node
        node.prev = self.start
        
        return node.value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self.get(key)
        else:
            if (self.current == self.capacity):
                last = self.end.prev
                self.end.prev = last.prev
                last.prev.next = self.end
                last.prev = None
                last.next = None
                del self.node_map[last.key]
                self.current = self.current - 1
                
            newNode = Node(key, value)
            self.node_map[key] = newNode
            newNode.next = self.start.next
            self.start.next.prev = newNode
            newNode.prev = self.start
            self.start.next = newNode
            self.current = self.current + 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
