#1

#2 With string.split()

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        num1 = version1.split('.')
        num2 = version2.split('.')
        num1 += [0] * (max(len(num1), len(num2)) - len(num1))
        num2 += [0] * (max(len(num1), len(num2)) - len(num2))
        i = 0
        while i < len(num1):
            if int(num1[i]) > int(num2[i]):
                return 1
            if int(num1[i]) < int(num2[i]):
                return -1
            else:
                i += 1
        if i == len(num1):
            return 0
