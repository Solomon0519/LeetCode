class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maximum = 0
        buyIndex = 0

        for sellIndex in range(1, len(prices)):
            boughtAt = prices[buyIndex]
            soldAt = prices[sellIndex]
            if soldAt > boughtAt:
                profit = soldAt - boughtAt
                maximum = max(maximum, profit)
            else:
                buyIndex = sellIndex


        return maximum