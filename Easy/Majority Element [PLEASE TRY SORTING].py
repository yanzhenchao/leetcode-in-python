#1 Sort first and return the middle value

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        num.sort()
        return num[len(num)/2]

#2 Assign the majority only when the count comes down to 0

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        m = 0
        c = 0
        for n in num:
            if c == 0:
                m = n
                c += 1
            else: # Same, count + 1. Different, count - 1.
                if m == n:
                    c += 1
                else:
                    c -= 1
        return m

#3 Hash Table

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        d = {n:0 for n in num}
        for n in num:
            d[n] += 1
            if d[n] > len(num) // 2:
                    return n
