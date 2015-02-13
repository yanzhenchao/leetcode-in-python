#1 Use min() and max(), calculate from right side

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        gain = 0
        if len(prices) > 0:
            high = 0
            for i in range(len(prices)-1, -1, -1):
                high = max(prices[i], high)
                diff = high - prices[i]
                gain = max(diff, gain)
        return gain

#2 Compare values to get minimal and maximal values

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        gain = 0
        if len(prices) > 0:
            low = prices[0]
            for i in range(len(prices)):
                if prices[i] < low:
                    low = prices[i]
                diff = prices[i] - low
                if diff > gain:
                    gain = diff
        return gain
