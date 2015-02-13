#1 map() is different for Python 2.x and 3.x

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        num = int(''.join(map(str, digits)))
        num += 1
        return list(map(int, str(num)))

#2 More Math

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        sum = 0
        for d in digits:
            sum += d
            total = sum + 1
            sum *= 10
        return [int(k) for k in str(total)]
