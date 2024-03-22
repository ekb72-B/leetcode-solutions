class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maximize the sell, minimize the buy . only keep max diff
        minprice = float('inf')
        profit = 0

        for price in prices:
            if price < minprice:
                minprice = price

            elif price - minprice > profit:
                profit = price - minprice

        return profit