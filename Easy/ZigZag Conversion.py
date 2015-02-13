#1 Change steps when reaching certain index

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows <= 1:
            return s
        new = [‘'] * nRows
        k = 0
        for i in range(len(s)):
            new[k] += s[i]
            if k == 0:
                step = 1
            if k == nRows - 1:
                step = -1
            k += step
        return ''.join(new)

#2 If the cycle is a multiple of 2, use %.

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows <= 1:
            return s
        new = ['']*nRows
        k = 0
        for i in range(len(s)):
            new[k] += s[i]
            if i / (nRows - 1) % 2 == 0:
                k += 1
            if i / (nRows - 1) % 2 == 1:
                k -= 1
        return ''.join(new)
