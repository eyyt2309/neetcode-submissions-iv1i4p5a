class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        n = len(matrix)
        m = len(matrix[0])

        def dfs(x, y):
            if (x, y) in dp: # if this cell already has a longest path, return it
                return dp[(x, y)]

            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            # dont think i need a visited set because path should be strictly longestIncreasingPath
            longest = 1

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:       # check bounds
                    if matrix[nx][ny] > matrix[x][y]: # strictly increasing
                        longest = max(longest, 1 + dfs(nx, ny)) # get longest path from neighbors

            dp[(x, y)] = longest
            return dp[(x, y)]

        highest = float('-inf')
        for x in range(n):
            for y in range(m):
                highest = max(highest, dfs(x, y))
        return highest


