# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and list2:
            return list2
        elif not list2 and list1:
            return list1

        node1 = head1
        node2 = head2

        dummy = ListNode()
        tail = dummy

        while node1 and node2:
            if node1.val <= node2.val:
                tail.next = node1
                node1 = node1.next
            else:
                tail.next = node2
                node2 = node2.next
            tail = tail.next

        if node1:
            tail.next = node1
        else:
            tail.next = node2
        
        return dummy.next



