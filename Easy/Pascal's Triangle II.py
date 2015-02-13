#1 Initialize a row as [1,…,1]. As row index increases, calculate from the last index.

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        row=[1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j-1]
        return row

#2 use the snippet in Pascal’s Triangle I

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        tri = []
        for i in range(0, rowIndex+1):
            tri += [[1]]
            for j in range(i-1):
                tri[i] += [tri[i-1][j] + tri[i-1][j+1]]
            if i >= 1:
                tri[i] += [1]
        return tri[rowIndex]
