class Solution(object):
    def reconstructQueue(self, people):
        """
        https://leetcode.com/problems/queue-reconstruction-by-height/description/
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        ret = []
        for i in range(len(people)):
            ret.insert(people[i][1], people[i])
        return ret
