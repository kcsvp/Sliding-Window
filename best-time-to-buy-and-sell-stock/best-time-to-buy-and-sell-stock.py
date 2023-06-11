class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minbuy = prices[0]
        for i in range(1,len(prices)):
            if prices[i]-minbuy > profit:
                profit = prices[i] - minbuy
            elif minbuy > prices[i]:
                minbuy = prices[i]
        return profit