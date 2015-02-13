#1 Use a counter here. Or Shorten the longer one first

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        valA = []
        valB = []
        currentA = headA
        currentB = headB
        while currentA:
            valA += [currentA.val]
            currentA = currentA.next
        while currentB:
            valB += [currentB.val]
            currentB = currentB.next
        k = 0
        while k < min(len(valA), len(valB)) and valA[-k-1] == valB[-k-1]:
            k += 1
        if k == 0:
            return None
        headC = headA
        for s in range(len(valA)-k, 0, -1):
            headC = headC.next
        return headC
