#1 Store the value in the given list from beginning

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = 0
        i = 0
        while i < len(A):
            A[n] = A[i]
            n += 1
            i += 1
            while i < len(A) and A[i-1] == A[i]:
                i += 1
        A = A [:n]
        return len(A)

#2 Swap the unequal items

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        i = 0
        j = 0
        while i < len(A):
            if A[i] != A[j]:
                A[i], A[j+1] = A[j+1], A[i]
                j += 1
            i += 1
        A = A[:j+1]
        return j+1
