class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers, store max on one side and min on other side
        ptr1 = 0
        ptr2 = 0
        maxprofit = 0

        while ptr2 < len(prices):
            currprofit = prices[ptr2] - prices[ptr1]
            if prices[ptr1] < prices[ptr2]:
                maxprofit = max(maxprofit, currprofit)
            else:
                ptr1 = ptr2
            ptr2 += 1
        
        return maxprofit
        
            