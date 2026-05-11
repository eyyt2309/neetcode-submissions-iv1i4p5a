# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        node = head
        arr = []

        while node:
            arr.append(node)
            node = node.next

        left = 0
        right = len(arr) - 1

        while True:
            arr[left].next = arr[right]
            left += 1

            if left >= right:
                arr[right].next = None
                break

            arr[right].next = arr[left]
            right -= 1

