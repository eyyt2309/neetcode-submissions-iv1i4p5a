# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def hasKNodes(node):
            # start from the 1st node and count k - 1 more nodes
            if not node:
                return False
            for _ in range(k - 1):
                node = node.next
                if not node:
                    return False
            return True
        
        def dfs(node):
            # if this node does not have k - 1 subsequent nodes, dont do the reversal
            if not hasKNodes(node):
                return node

            end = node
            curr = node
            prev = None
            for _ in range(k):
                next = curr.next
                curr.next = prev

                prev = curr
                curr = next

            end.next = dfs(curr)
            return prev
        return dfs(head)



             