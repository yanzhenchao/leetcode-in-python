#1 Create two stacks. One regular and one for minimum.

class MinStack:
    def __init__(self):
        self.stack = []
        self.stackMin = []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if not self.stackMin or x <= self.stackMin[-1]:
            self.stackMin.append(x)

    # @return nothing
    def pop(self):
        pop = self.stack.pop()
        if pop == self.stackMin[-1]:
            self.stackMin.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.stackMin[-1]
