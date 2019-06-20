class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = collections.Counter()
        for answer in answers:
            cnt[answer] += 1
        ret = cnt.get(0, 0)
        # print(cnt)
        for key in cnt:
            if key == 0:
                continue
            else:
                ret += (key + 1)*math.ceil((cnt[key]/(key+1)))
        return ret