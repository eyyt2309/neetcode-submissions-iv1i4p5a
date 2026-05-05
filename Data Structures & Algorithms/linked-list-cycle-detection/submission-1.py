# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        nodes_visited = {}

        node = head

        while node:
            if node not in nodes_visited:
                nodes_visited[node] = 1
            elif node in nodes_visited:
                return True

            node = node.next

        return False