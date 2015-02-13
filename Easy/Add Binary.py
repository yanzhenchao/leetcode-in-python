#1 Remove leading ‘0b’ for binary numbers

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        return str(bin(int(a, 2)+int(b, 2))[2:])

#2 Add digits manually 

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        # A list of sum of each digit
        c = list(map(int, str(int(a) + int(b))))
        # Create a reversed string d
        d = ''
        for k in range(len(c)-1, 0, -1):
            if c[k] < 2:
                d += str(c[k])
            else:
                d += str(c[k]-2)
                c[k-1] += 1
        # Add the leading digit
        if c[0] < 2:
            d += str(c[0])
        else:
            d += str(c[0]-2) + '1'
        return d[::-1]
