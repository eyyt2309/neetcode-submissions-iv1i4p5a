class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = {}
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        def dfs(x, y):
            if x >= n or y >= m: # out of bounds
                return 0
            if obstacleGrid[x][y] == 1: # obstacles should return 0
                return 0
            if x == n - 1 and y == m - 1: # bottom right found
                return 1
            if (x, y) in dp:
                return dp[(x, y)]

            directions = [(1,0), (0, 1)] # move right or down

            paths = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                paths += dfs(nx, ny)
            dp[(x, y)] = paths
            return paths

        return dfs(0, 0)


            