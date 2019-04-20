class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        # https://leetcode.com/problems/add-bold-tag-in-string
        if not dict:
            return s
        def find_all(a_str, sub):
            start = 0
            while True:
                start = a_str.find(sub, start)
                if start == -1: return -1
                yield start
                start += 1
        pl = positions_and_lengths = []
        count = 0
        for string in dict:
            pos = find_all(s, string)
            if pos != -1:
                for position in pos:
                    positions_and_lengths.append([position, position+len(string)])
                    count += 1
        # print(positions_and_lengths, pl)
        if count == 0:
            return s
        if count == 1:
            return s[:pl[0][0]] + '<b>' + s[pl[0][0]:pl[0][1]] + '</b>' + s[pl[0][1]:]
        pl.sort(key=lambda x: x[0])
        merged = [pl[0]]
        for i in range(1, len(pl)):
            # if pl[i][1]
            if pl[i][0] <= merged[-1][1]:
                merged[-1][1] = max(pl[i][1], merged[-1][1])
            else:
                merged.append(pl[i])
        offset = 0
        # print(merged)

        for interval in merged:
            # print(interval, offset, '1', s[:offset+interval[0]], '2', s[offset+interval[0]:offset+interval[1]], '3', s[offset+interval[1]:])
            s = s[:offset+interval[0]] + '<b>' + s[offset+interval[0]:offset+interval[1]] + '</b>' + s[offset+interval[1]:]
            offset += 7
            # print(s, offset)
        return s
