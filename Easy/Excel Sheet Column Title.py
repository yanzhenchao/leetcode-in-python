#1 Base 26. Modify num to access to list and make space for 0

class Solution:
    # @return a string
    def convertToTitle(self, num):
        letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        title = ''
        while num > 0:
            title = letter[(num-1)%26]+ title
            num = (num-1)/26
        return title

#2 When it comes to ‘Z’, make num minus 1

class Solution:
    # @return a string
    def convertToTitle(self, num):
        letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        title = ''
        while num != 0:
            r = num % 26
            num /= 26
            if r == 0:
                title = 'Z' + title
                num -= 1
            else:
                title = letter[r-1] + title
        return title

#3 Too complicated

class Solution:
    # @return a string
    def convertToTitle(self, num):
        letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        n = 0
        total = 0
        while total <= num:
            total += 26**n
            n += 1
        title = ''
        while n >= 3:
            if num%26 == 0:
                title += letter[(num/(26**(n-2)) - 2)%26]
            else:
                title += letter[(num/(26**(n-2)) - 1)%26]
            n -= 1
        title += letter[(num - 1)%26]
        return title
