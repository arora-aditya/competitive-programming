class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # https://leetcode.com/problems/compare-version-numbers/
        version1 = version1.split('.')
        version2 = version2.split('.')
        le1, le2 = len(version1), len(version2)
        if le1 < le2:
            version1 += [0] * (le2 - le1)
            le1 = le2
        else:
            version2 += [0] * (le1 - le2)
            le2 = le1
        i,j = 0,0

        while i < le1 and j < le2:
            v1, v2 = int(version1[i]), int(version2[j])
            # print(v1, v2)
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
            i += 1
            j += 1
        return 0
