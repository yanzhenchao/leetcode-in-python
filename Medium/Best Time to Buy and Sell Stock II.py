#1 Easy. Always buy low sell high.

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        diff = 0
        for i in range(0, len(prices)-1):
            if prices[i] < prices[i+1]:
                diff += prices[i+1] - prices[i]
        return diff
