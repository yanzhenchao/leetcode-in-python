#1 Manipulate multiplication from the last index.

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        new = [0] * (len(num1) + len(num2)-1)
        for i in range(len(num1)):
            for j in range(len(num2)):
                new[len(new)-1-i-j] += int(num1[len(num1)-1-i]) * int(num2[len(num2)-1-j])
        k = len(new) - 1
        while k > 0:
            new[k-1] += new[k] / 10
            new[k] = new[k] % 10
            k -= 1
        while len(new) > 1 and new[0] == 0:
            del new[0]
        return ''.join(list(map(str, new)))

#2 Python can handle infinite precision for integers.

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        return str(int(num1)*int(num2))

#3 Reverse the string first, and reverse the result in the end.

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        num1 = num1[ : :-1]
        num2 = num2[ : :-1]
        new = [0] * (len(num1) + len(num2)-1)
        for i in range(len(num1)):
            for j in range(len(num2)):
                new[i+j] += int(num1[i]) * int(num2[j])
        k = 0
        while k < len(new) - 1:
            new[k+1] += new[k] / 10
            new[k] = new[k] % 10
            k += 1
        while len(new) > 1 and new[len(new) - 1] == 0:
            del new[len(new) - 1]
        return ''.join(list(map(str, new[ : :-1])))
