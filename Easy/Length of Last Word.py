#1 Use split()

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        new = s.split()
        if len(new) == 0:
            return 0
        else:
            return len(new[-1])
