#1 Without Extra Space

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            temp = 1
            while x/temp >= 10:
                temp *= 10
            while temp > 1 :
                left = (x / temp) % 10
                right = x % 10
                if left != right:
                    return False
                x /= 10
                temp /= 100
            return True

#2 With Extra Space

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
