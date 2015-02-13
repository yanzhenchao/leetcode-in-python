#1 Simple and best

class Solution:
    # @return a string
    def intToRoman(self, num):
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ''
        for i in range(len(roman)):
            while num >= number[i]:
                result += roman[i]
                num -= number[i]
        return result

#2 Too complicated

class Solution:
    # @return a string
    def intToRoman(self, num):
        roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        number = [1000, 500, 100, 50, 10, 5, 1]
        convert1 = {'DCCCC':'CM',  'LXXXX':'XC',  'VIIII':'IX'}
        convert2 = {'CCCC':'CD', 'XXXX':'XL','IIII':'IV'}
        r = ''
        for i in range(len(number)):
            if num == number[i]:
                r += roman[i]
                break
            else:
                if num > number[i]:
                    count = int(num / number[i])
                    r += roman[i]*count
                    num -= number[i]*count
        for c in convert1:
            if c in r:
                r = r.replace(c, convert1[c])
        for c in convert2:
            if c in r:
                r = r.replace(c, convert2[c])
        return r
