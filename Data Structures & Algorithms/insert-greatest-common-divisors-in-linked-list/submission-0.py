# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        tail = dummy
        curr = tail.next
        # [12, 3, 4, 6]

        while curr.next:
            tail = curr
            curr = curr.next

            gcd = math.gcd(tail.val, curr.val)
            gcd_node = ListNode(gcd)

            tail.next = gcd_node
            gcd_node.next = curr
        return head


        