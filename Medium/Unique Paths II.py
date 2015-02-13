#1 Initialize the first row and first column

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid); n = len(obstacleGrid[0])
        d = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                d[i][0] = 1
            else:
                d[i][0] == 0
                break
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                d[0][i] = 1
            else:
                d[0][i] = 0
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1: d[i][j] = 0
                else:
                    d[i][j] = d[i-1][j] + d[i][j-1]
        return d[m-1][n-1]
