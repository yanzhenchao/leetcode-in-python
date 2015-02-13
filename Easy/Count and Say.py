#1

class Solution:
    # @return a string
    def countAndSay(self, n):
        s = ['1'] + [''] * (n-1)
        for i in range(0, n-1):
            j = 0
            while j < len(s[i]):
                temp = 1
                while j < len(s[i]) - 1 and s[i][j] == s[i][j+1]:
                    temp += 1
                    j += 1
                s[i+1] += str(temp) + s[i][j]
                j += 1
        return s[n-1]

#2

class Solution:
    # @return a string
    def countAndSay(self, n):
        s = '1'
        for i in range(n-1):
            left = new = ''
            num = 0
            for n in s:
                if left != '' and left != n:
                    new += str(num) + left
                    num = 1
                else:
                    num += 1
                left = n
            new += str(num) + left
            s = new
        return s
