class Solution:
    def key(self, log):
        id, rest = log.split(" ", 1)
        return (0, rest, id) if rest[0].isalpha() else (1,)

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # https://leetcode.com/problems/reorder-data-in-log-files/
        return sorted(logs, key = self.key)