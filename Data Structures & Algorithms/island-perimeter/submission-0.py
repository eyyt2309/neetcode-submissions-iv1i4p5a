from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        perimeter = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        n, m = len(grid), len(grid[0])

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1 and (r, c) not in visited:
                    queue = deque([(r, c)])
                    visited.add((r, c))

                    while queue:
                        r, c = queue.popleft()
                        base_perimeter = 4

                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc

                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                                base_perimeter -= 1
                                if (nr, nc) not in visited:
                                    queue.append((nr, nc))
                                    visited.add((nr, nc))

                        perimeter += base_perimeter
        
        return perimeter


        