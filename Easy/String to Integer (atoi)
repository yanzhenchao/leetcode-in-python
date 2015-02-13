#1 Read the specification carefully.

class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        new = ''
        i = 0
        while i < len(str) and ((i == 0 and str[i] in '+-') or str[i].isdigit()):
            new += str[i]
            i += 1
        if new in '+-':
            return 0
        else:
            result = int(new)
        if result > 2**31-1:
            return 2**31-1
        if result > -2**31-1:
            return result
        else:
            return -2**31

#2 More code. 

class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        if len(str) == 1 and str.isdigit():
            return int(str)
        elif len(str) > 1 and ( str[0].isdigit() or ( str[0] in '-+' and str[1].isdigit() ) ):
            i = 1
            new = str[0]
            while i<len(str) and str[i].isdigit():
                new += str[i]
                i += 1
            if int(new) > 2**31-1:
                return 2**31-1
            elif int(new) > -2**31-1:
                return int(new)
            else:
                return -2**31
        else:
            return 0
