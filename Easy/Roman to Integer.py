#1 The left character can be taken as negative value. Reverse the string first.

class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s[::-1]
        num = 0
        temp = 0
        for c in s:
            if roman[c] >= temp:
                num += roman[c]
            else:
                num -= roman[c]
            temp = roman[c]
        return num

#2 Create a longer dictionary

class Solution:
    # @return an integer
    def romanToInt(self, s):
        dictRoman = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        i = 0
        num = 0
        while i < len(s) :
            if i < len(s) - 1 and (s[i] + s[i+1]) in dictRoman:
                num += dictRoman[s[i] + s[i+1]]
                i += 2
            else:
                num += dictRoman[s[i]]
                i += 1
        return num
