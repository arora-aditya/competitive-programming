class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        https://leetcode.com/problems/keys-and-rooms/description/
        :type rooms: List[List[int]]
        :rtype: bool
        """
        ans = []
        level = rooms[0]
        le = len(rooms)
        unlocked = [False]*le
        unlocked[0] = True
        cn = 1
        while level:
            # print(level)
            temp = set()
            for i in level:
                if unlocked[i] == False:
                    unlocked[i] = True
                    cn += 1
                temp |= set(rooms[i])
                rooms[i] = []
            level = temp
        return cn == le
