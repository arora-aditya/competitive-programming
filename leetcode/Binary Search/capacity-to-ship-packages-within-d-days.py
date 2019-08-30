class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
        def guess(capacity):
            rounds, curr = 1, 0
            for w in weights:
                curr += w
                if curr > capacity:
                    curr = w
                    rounds += 1
                    if rounds > D:
                        return False
            return True
        
        low = max(math.ceil(sum(weights)/D), max(weights))
        high = math.ceil(len(weights)/D) * max(weights)
        
        while low <= high:
            mid = (low + high) // 2
            if guess(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low