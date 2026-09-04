# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        """[dummy, 1, 2, 3, 4, 5] """
        if left == right:
            return dummy.next

        # reach start of reversed nodes
        for _ in range(left):
            tail = curr
            curr = curr.next
        left_prev = tail

        left_end = curr # store end of reversed nodes

        for _ in range(left, right):
            next = curr.next
            curr.next = tail
            tail = curr
            curr = next

        # set new end of reversed node to next of curr
        left_end.next = curr.next
        curr.next = tail
        left_prev.next = curr

        return dummy.next
        
        
