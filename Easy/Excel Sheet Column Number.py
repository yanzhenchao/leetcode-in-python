#1 base 26. Multiply index + 1 for each position

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        all = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num = 0
        for i in range(len(s)):
            for j in range(len(all)):
                if s[i] == all[j]:
                    num += (j+1) * 26 ** (len(s) - i - 1)
        return num

#2 Convert base 26 to base 10

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        all = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
        n = 0
        num = 0
        while n < len(s):
            num *= 26
            num += all[s[n]]
            n += 1
        return num
