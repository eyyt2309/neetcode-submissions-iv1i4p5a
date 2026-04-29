from collections import deque

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
        
        node_dict = {}
        stack = deque()
        
        if head is None:
            return None

        node = head
        stack.append(node)

        while stack:
            node = stack.pop()

            # if node not in hashmap, create new node
            if node is not None and node not in node_dict:
                new_node = Node(node.val)
                node_dict[node] = new_node
            # take existing node from hashmap and update next and random
            elif node is not None and node in node_dict:
                new_node = node_dict[node]


            if node.next is not None and node.next not in node_dict:
                next_new_node = Node(node.next.val)
                node_dict[node.next] = next_new_node
                new_node.next = next_new_node
                stack.append(node.next)
            elif node.next is not None and node.next in node_dict:
                new_node.next = node_dict[node.next]

            if node.random is not None and node.random not in node_dict:
                random_new_node = Node(node.random.val)
                node_dict[node.random] = random_new_node
                new_node.random = random_new_node
                stack.append(node.random)
            elif node.random is not None and node.random in node_dict:
                new_node.random = node_dict[node.random]
        
        return node_dict[head]

        