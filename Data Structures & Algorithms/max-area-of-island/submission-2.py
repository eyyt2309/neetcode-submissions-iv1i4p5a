class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = float('-inf')
        rows = len(grid)
        cols = len(grid[0])
        visited = {}

        def dfs(x, y):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            descendentArea = 0

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == 1 and (nx, ny) not in visited:
                        visited[(nx, ny)] = True
                        descendentArea += dfs(nx, ny)

            return 1 + descendentArea

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1 and (x, y) not in visited:
                    visited[(x, y)] = True
                    area = dfs(x, y)
                    self.maxArea = max(area, self.maxArea)

        if self.maxArea == float('-inf'):
            return 0
        else:
            return self.maxArea

