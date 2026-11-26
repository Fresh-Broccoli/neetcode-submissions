class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min = prices[0]
        max_profit = 0
        for price in prices[1:]:
            profit = price - left_min
            max_profit = max(profit, max_profit)
            left_min = min (left_min, price)
        return max_profit