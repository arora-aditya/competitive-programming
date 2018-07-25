class Solution:
    def numRescueBoats(self, people, limit):
        """
        https://leetcode.com/problems/boats-to-save-people/description/
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans
        
