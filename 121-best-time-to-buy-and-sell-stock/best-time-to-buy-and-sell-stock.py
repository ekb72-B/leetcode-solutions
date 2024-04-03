class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = float("-inf")
        minseen = float("inf")

        for price in prices:
            minseen = min(price, minseen)
            maxprof = max(maxprof, price - minseen)

        return maxprof

       