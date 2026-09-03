from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        n = len(grid)
        m = len(grid[0])

        for x in range(n):
            for y in range(m):
                if grid[x][y] == 0: # add treasure chests to stack
                    queue.append((x, y))

        print(queue)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            x, y = queue.popleft() # get cell
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == 2147483647:
                        grid[nx][ny] = min(1 + grid[x][y], grid[nx][ny])
                        queue.append((nx, ny))

        
