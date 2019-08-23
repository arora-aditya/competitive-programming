class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # https://leetcode.com/problems/reveal-cards-in-increasing-order/
        N = len(deck)
        index = collections.deque(range(N))
        ans = [None] * N

        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())

        return ans