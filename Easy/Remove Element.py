#1 Count the times of adding number in A

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        n = 0
        for c in A:
            if c != elem:
                A[n] = c
                n +=  1
        A = A[:n]
        return n

#2 Use list.remove()

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        while elem in A:
            A.remove(elem)
        return len(A)
