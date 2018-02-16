class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]
