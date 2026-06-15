"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}

        node = head

        if not head:
            return None

        while node:
            if node not in node_map:
                node_map[node] = Node(node.val) 

            if node.next not in node_map and node.next is not None:
                node_map[node.next] = Node(node.next.val)
                node_map[node].next = node_map[node.next]
            elif node.next in node_map:
                node_map[node].next = node_map[node.next]
            else:
                node_map[node].next = None

            if node.random not in node_map and node.random is not None:
                node_map[node.random] = Node(node.random.val)
                node_map[node].random = node_map[node.random]
            elif node.random in node_map:
                node_map[node].random = node_map[node.random]
            else:
                node_map[node].random = None

            node = node.next

        return node_map[head]