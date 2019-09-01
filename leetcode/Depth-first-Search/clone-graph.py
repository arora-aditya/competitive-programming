"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    di = {}
    def cloneGraph(self, node):
        # https://leetcode.com/problems/clone-graph/
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node

        if node in self.di:
            return self.di[node]

        new_node = Node(node.val, [])
        self.di[node] = new_node

        if node.neighbors:
            new_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return new_node
            
                