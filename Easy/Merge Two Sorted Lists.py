#1 Linked lists are mutable. Just define each node.

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        fake = ListNode(0)
        temp = fake
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
                temp = temp.next
            else:
                temp.next = l2
                l2 = l2.next
                temp = temp.next
        if not l1:
            temp.next = l2
        if not l2:
            temp.next = l1
        return fake.next
