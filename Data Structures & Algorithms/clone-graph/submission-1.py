"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        node_map = {}
        visited = set()
        queue = deque([node])
        visited.add(node) # add current node to visited set
        node_map[node] = Node(node.val)

        while True:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in node_map: # if neighbor node not in map, create it
                    node_map[neighbor] = Node(neighbor.val)
                node_map[curr].neighbors.append(node_map[neighbor]) # append to adj list of current node
                
                if neighbor not in visited: # add neighbor to queue if not explored yet
                    visited.add(neighbor)
                    queue.append(neighbor)
            
            if not queue:
                break
        
        return node_map[node]

        