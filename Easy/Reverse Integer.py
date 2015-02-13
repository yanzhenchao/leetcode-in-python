#1 Convert to string first

class Solution:
    # @return an integer
    def reverse(self, x):
        sign = (-(-1)**(x>=0))
        s = str(abs(x))
        r = ''
        for i in range(len(s)-1, -1, -1):
            r += s[i]
        r = int(r)
        return r * (r < 2**31)

#2 Short version, reversed() returns a object

class Solution:
    # @return an integer
    def reverse(self, x):
        sign = (-(-1)**(x>=0))
        new = int(''.join(map(str, reversed(str(abs(x))))))
        return (new < 2**31)* new
