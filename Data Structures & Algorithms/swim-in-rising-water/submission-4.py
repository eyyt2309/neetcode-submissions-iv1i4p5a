from heapq import heappush, heappop
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        n = len(grid)
        heap.append((grid[0][0], 0, 0))
        visited = set()
        visited.add((0, 0))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]


        while heap:
            t, r, c = heappop(heap)

            if r == n - 1 and c == n - 1:
                return t

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if (nr, nc) not in visited:
                        heappush(heap, (max(grid[nr][nc], t), nr, nc))
                        visited.add((nr, nc))
        

            

            