class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # buy - > lowest 
        min_price = prices[0] + fee
        max_profit = 0

        for price in prices:
            # if curr price > min price, profit can be made
            if min_price < price:
                max_profit += price - min_price
                min_price = price

            elif min_price > price + fee:
                min_price = price + fee

        return max_profit
        