class Solution:
    def maxProfit(self, prices):
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        profit = 0
        currMin = prices[0]

        for p in prices:
            if p> currMin:
                profit = max(p - currMin, profit)
            else:
                currMin = p

        return profit
