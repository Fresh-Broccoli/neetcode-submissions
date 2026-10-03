class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest,gains = prices.pop(0),0
        for price in prices:
            profit = price - lowest
            if lowest > price:
                lowest = price
            if profit > gains:
                gains = profit
        return gains