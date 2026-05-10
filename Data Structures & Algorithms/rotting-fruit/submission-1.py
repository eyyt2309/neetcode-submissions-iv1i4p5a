from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        count = 0
        total = 0
        min_time = 0

        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    total += 1
                if grid[row][col] == 2:
                    total += 1
                    queue.append((row, col, 0))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while queue:
            count += 1
            row, col, time = queue.popleft()
            if time > min_time:
                min_time = time

            for direction in directions:
                dr, dc = direction
                nr, nc = row + dr, col + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1:
                        queue.append((nr, nc, time + 1))
                        grid[nr][nc] = 2

        if count != total:
            return -1
        else:
            return min_time