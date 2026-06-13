# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        carry = 0

        while l1 and l2:
            add = l1.val + l2.val + carry
            if carry == 1:
                carry = 0
            if add >= 10:
                add = add % 10
                carry = 1
        
            l1 = l1.next
            l2 = l2.next
            
            tail.next = ListNode(add)
            tail = tail.next

        while l1:
            add = l1.val + carry
            if carry == 1:
                carry = 0
            if add >= 10:
                add = add % 10
                carry = 1
            l1 = l1.next
            tail.next = ListNode(add)
            tail = tail.next

        while l2:
            add = l2.val + carry
            if carry == 1:
                carry = 0
            if add >= 10:
                add = add % 10
                carry = 1
            l2 = l2.next
            tail.next = ListNode(add)
            tail = tail.next

        if carry:
            tail.next = ListNode(carry)
            tail = tail.next

        return head.next

            