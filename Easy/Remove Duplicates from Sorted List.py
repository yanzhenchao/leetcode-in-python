#1 Without creating a new list

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                temp = current.next
                current.next = current.next.next # current.next property .next
                del temp # del the node in between
            else:
                current = current.next
        return head

#2 Creating a new list

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return head
        values = []
        current = head
        while current:
            if current.val not in values:
                values += [current.val]
            current = current.next
        new = ListNode(0)
        temp = new
        for v in values:
            temp.next = ListNode(v)
            temp = temp.next
        return new.next
