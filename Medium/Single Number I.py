#1 XOR to find the singe. x ^ 0 = x, x ^ x = 0.

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        s = 0
        for c in A:
            s = s ^ c
        return s
