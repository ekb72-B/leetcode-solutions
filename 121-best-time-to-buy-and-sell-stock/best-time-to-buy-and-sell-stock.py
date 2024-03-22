class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maximize the sell, minimize the buy . only keep max diff
        buy = prices[0]
        sell = 0
        profit = 0

        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell-buy)
            else:
                buy = sell

        return profit