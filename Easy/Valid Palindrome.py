#1 Replace non-alphanumaric characters with ''

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        for c in s:
            if not c.isalnum():
                s = s.replace(c, '')
        if s.lower() != s.lower()[::-1]:
            return False
        return True

#2 Create a new string with alphanumeric characters

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        new = ''
        for c in s:
            if c.isalnum():
                new += c
        new = new.lower()
        for i in range(len(new)/2):
            if new[i] != new[len(new)-1-i]:
                return False
        return True

