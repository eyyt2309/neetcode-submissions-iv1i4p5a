from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = {}

        islands = []

        stack = deque()

        rows = len(grid)
        cols = len(grid[0])

        neighbors = [(1,0),(-1,0),(0,1),(0,-1)]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in visited:
                    area = 0
                    stack.append((row,col))
                    visited[(row,col)] = 1

                    while stack:
                        r,c = stack.pop()
                        area += 1
                        for dr, dc in neighbors:
                            nr = r + dr
                            nc = c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr , nc) not in visited:
                                visited[(nr,nc)] = 1
                                stack.append((nr, nc))
                    
                    islands.append(area)

        if len(islands) > 0:
            return max(islands)
        else:
            return 0                             
