from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        fresh = 0
        queue = deque()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        rows = len(grid)
        cols = len(grid[0])

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 2:
                    queue.append((x, y))
                elif grid[x][y] == 1:
                    fresh += 1

        while queue:
            n = len(queue)
            for _ in range(n):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh -= 1
            if queue:
                minutes += 1
        
        if fresh != 0:
            return -1
        else:
            return minutes