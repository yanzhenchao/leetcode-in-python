#1 Add all [1…1] for each row

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        tri = []
        for i in range(numRows):
            tri +=[[1]*(i+1)]
        for i in range(1, numRows):
            for j in range(i - 1, 0, -1):
                tri[i][j] = tri[i-1][j] + tri[i-1][j-1]
        return tri

#2 Add [1] as the program executes

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        tri = []
        for i in range(0, numRows):
            tri += [[1]]
            for j in range(i-1):
                tri[i] += [tri[i-1][j] + tri[i-1][j+1]]
            if i >= 1:
                tri[i] += [1]
        return tri

#3 Initial all basic elements in tri list as 1

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        tri = [[1]]*numRows
        for i in range(1, numRows):
            for j in range(i-1, 0, -1):
                tri[i] = [tri[i-1][j] + tri[i-1][j-1]] + tri[i]
            tri[i] = [1]+ tri[i]
        return tri
