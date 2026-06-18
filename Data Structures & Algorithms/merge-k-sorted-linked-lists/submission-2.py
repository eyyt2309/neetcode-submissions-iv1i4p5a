import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        tail = head

        heap = []
        
        counter = 0
        for heads in lists:
            if head:
                heapq.heappush(heap, (heads.val, counter, heads))
                counter += 1

        

        while heap:
            # pop min node from top
            val, counter, node = heapq.heappop(heap)
            next_node = node.next
            
            tail.next = node

            if next_node:
                heapq.heappush(heap, (next_node.val, counter, next_node))
                counter += 1

            tail = tail.next

        return head.next





        
        