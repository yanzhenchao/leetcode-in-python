#1 Shorter version

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        left = '([{'
        right = ')]}'
        for p in s:
            if p in left:
                stack.append(p);
            else:
                if not stack or stack.pop() != left[right.index(p)]:
                    return False
        return not stack

#2 Use a stack to store parenthesizes

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] in '([{':
                stack.append(s[i])
            if s[i] == ')':
                if not stack or stack.pop() != '(':
                    return False
            if s[i] == ']':
                if not stack or stack.pop() != '[':
                    return False
            if s[i] == '}':
                if not stack or stack.pop() != '{':
                    return False
        return not stack

#3 More clear about stack.pop()

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        left = '([{'
        right = ')]}'
        for p in s:
            if p in left:
                stack.append(p);
            for i in range(3):
                if p == right[i]:
                    if not stack or stack[-1] != left[i]:
                        return False
                    else:
                        stack.pop();
        return not stack
