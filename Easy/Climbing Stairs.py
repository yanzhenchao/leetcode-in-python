#1 Short initial dp list

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        dp = [0, 1, 2]
        i = 3
        while i <= n:
            dp += [dp[i-1]+dp[i-2]]
            i += 1
        return dp[n]

#2 Long initial dp list

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        dp = [i for i in range(n+1)]
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
