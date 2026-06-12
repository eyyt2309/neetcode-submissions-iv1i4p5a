# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2

        head = ListNode()
        tail = head

        while node1 and node2:
            if node1.val < node2.val:
                tail.next = node1
                node1 = node1.next
                tail = tail.next
            else:
                tail.next = node2
                node2 = node2.next
                tail = tail.next
        while node1:
            tail.next = node1
            node1 = node1.next
            tail = tail.next
        while node2:
            tail.next = node2
            node2 = node2.next
            tail = tail.next
        return head.next