class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        greatest_profit = 0
        min_price = float(99999.0)
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > greatest_profit:
                greatest_profit = price - min_price
                
        return greatest_profit
        