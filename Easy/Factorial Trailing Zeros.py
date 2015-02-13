#1 The number of zeros is the sum of the weight of all as power of 5

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        zeros = 0
        while n >= 5:
            zeros += n/5
            n /= 5
        return zeros

#3 Too complicated

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        if n == 0:
            return 0
        zeros = 0
        m = 0
        temp = n/5
        while temp >= 1:
            m += 1
            temp /= 5
        for i in range(m):
            zeros += n/5**(i+1)
        return zeros
