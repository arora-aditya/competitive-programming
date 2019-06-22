from collections import defaultdict
class Node:
    def __init__(self, val, neighbour):
        self.val = val
        self.neighbours = set()
    def addNeighbour(self, neighbour):
        self.neighbours |= set([neighbour])
        
    def findAllNeighbours(self):
        visited , stack = set(), [self]
        while stack:
            node = stack.pop()
            if node.val not in visited:
                visited.add(node.val)
                stack.extend(node.neighbours)
        return visited

    def __str__(self):
        return f'{self.val} {[x.val for x in self.neighbours]}'
            

class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        di = {}
        for word1, word2 in pairs:
            if word1 in di:
                n1 = di[word1]
            else:
                n1 = Node(word1, word2)
            if word2 in di:
                n2 = di[word2]
            else:
                n2 = Node(word2, word1)
            n1.addNeighbour(n2)
            n2.addNeighbour(n1)
            di[word1] = n1
            di[word2] = n2

        dic = defaultdict(set)
        for word in di:
            if word not in dic:
                dic[word] = di[word].findAllNeighbours()
                for neighbour in dic[word]:
                    dic[neighbour] = dic[word]
        
        
        for i in range(len(words1)):
            word1 = words1[i]
            word2 = words2[i]
            if len(dic[word1] & dic[word2]) == 0 and word1 != word2:
                return False
        return True