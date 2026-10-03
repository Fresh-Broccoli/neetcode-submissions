class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, highest, gains = prices.pop(0), -1, 0
        for price in prices:
            profit = price - lowest
            if lowest > price:
                lowest = price
            if profit > gains:
                gains = profit
        return gains