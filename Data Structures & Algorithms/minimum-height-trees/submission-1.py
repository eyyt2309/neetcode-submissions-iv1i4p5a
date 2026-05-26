from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        edges_set = set(map(tuple, edges))
        tree_dict = {}
        minheight = float('inf')

        def dfs(node, visited = None):
            if visited == None:
                visited = [0 for _ in range(n)]
                visited[node] = 1
            neighbors = self.getNeighbors(node, edges_set, visited)
            if not neighbors:
                return 0
            height = 0
            for neighbor in neighbors:
                visited[neighbor] = 1
                height = max(height, dfs(neighbor, visited) + 1)
            return height

        for node in range(n):
            node_height = dfs(node)
            tree_dict[node] = node_height
            minheight = node_height if node_height < minheight else minheight

        ans = []
        for node in tree_dict:
            if tree_dict[node] == minheight:
                ans.append(node)

        return ans

    # get neighbors that have not been visited
    def getNeighbors(self, node, edges_set, visited):
        neighbor = []
        for u, v in edges_set:
            if u == node:
                if visited[v] == 0:
                    neighbor.append(v)
            elif v == node:
                if visited[u] == 0:
                    neighbor.append(u)
        return neighbor
        
