#1 Use Math

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        # Total steps
        N = m - 1 + n - 1
        # C(N, k) == C(N, N - k)
        k = min(m,n) - 1
        result = 1
        for i in range(k):
            result = result * (N - i)/(i + 1)
        return result

#2 Use Dynamic Programming

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        d = [[0]*n]*m
        for i in range(0, m):
            d[i][0] = 1
        for j in range(0, n):
            d[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = d[i-1][j] + d[i][j-1]
        return d[m-1][n-1]
