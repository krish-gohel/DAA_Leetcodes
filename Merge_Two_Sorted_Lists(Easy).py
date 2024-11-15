class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to serve as the start of the merged list
        dummy = ListNode()
        current = dummy

        # Pointers for the two lists
        p1 = list1
        p2 = list2

        # Traverse through both lists
        while p1 and p2:
            if p1.val < p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next

        # If there are remaining nodes in either list, append them
        if p1:
            current.next = p1
        if p2:
            current.next = p2

        # The merged list is in dummy.next
        return dummy.next