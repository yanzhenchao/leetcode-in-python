#1 Count the length of the list. Get a helper dummy and temp

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        current = head
        k = 0
        while current.next:
            current = current.next
            k += 1
        m = 0
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        while m < k + 1 - n:
            temp = temp.next
            m += 1
        temp.next = temp.next.next
        return dummy.next

#2 Use two pointers. More convenient.

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        fast = slow = dummy = ListNode(0)
        dummy.next = head
        i = 0
        while i < n and fast:
            fast = fast.next
            i += 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
