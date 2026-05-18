from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {node: Node(node.val)}
        stack = deque()
        stack.append(node)

        while stack:
            cur = stack.pop()

            for neighbor in cur.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                clones[cur].neighbors.append(clones[neighbor])

        return clones[node]
    

            
            

