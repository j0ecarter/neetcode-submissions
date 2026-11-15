class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_day = 0
        n = len(prices)

        while buy_day < n - 1:
            while buy_day < n - 1 and prices[buy_day + 1] <= prices[buy_day]:
                buy_day += 1

            sell_day = buy_day
            while sell_day < n - 1 and prices[sell_day + 1] >= prices[sell_day]:
                sell_day += 1

            max_profit += prices[sell_day] - prices[buy_day]
            buy_day = sell_day + 1

        return max_profit