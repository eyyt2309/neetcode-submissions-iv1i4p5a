# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        place = 0
        total = 0

        temp = ListNode()
        head = temp

        while l1 is not None and l2 is not None:
            total += (l1.val * (10 ** place))

            total += (l2.val * (10 ** place))

            place += 1

            l1 = l1.next
            l2 = l2.next


        while l1 is not None:
            total += (l1.val * (10 ** place))
            place += 1
            l1 = l1.next

        while l2 is not None:
            total += (l2.val * (10 ** place))
            place += 1
            l2 = l2.next

        while total != 0:
            digit = total % 10
            total = total // 10
            temp.val = digit

            if total != 0:
                temp.next = ListNode()
                temp = temp.next

        return head
