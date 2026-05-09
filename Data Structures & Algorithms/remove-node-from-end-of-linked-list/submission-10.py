# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []

        node = head

        while node:
            arr.append(node)
            node = node.next

        if n == len(arr):
            return head.next
        elif n == 1:
            if len(arr) == 1:
                return None
            else:
                arr[-2].next = None
                return head
        else:
            arr[-n - 1].next = arr[-n + 1]
            return head

