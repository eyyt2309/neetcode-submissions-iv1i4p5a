from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        stack = deque()

        memo = [[None for _ in range(cols)] for _ in range(rows)]
        count = 0

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for row in range(rows):
            if grid[row][0] == 1:
                stack.append((row, 0))
            if grid[row][cols - 1] == 1:
                stack.append((row, cols - 1))

        for col in range(cols):
            if grid[0][col] == 1:
                stack.append((0, col))
            if grid[rows - 1][col] == 1:
                stack.append((rows - 1, col))
                
        while stack:
            r, c = stack.pop()
            memo[r][c] = 1

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows - 1 and 0 <= nc < cols - 1 and grid[nr][nc] == 1:
                    if memo[nr][nc] is None:
                        stack.append((nr, nc))

        for row in range(1, rows):
            for col in range(1, cols):
                if grid[row][col] == 1 and memo[row][col] == None:
                    count += 1

        return count