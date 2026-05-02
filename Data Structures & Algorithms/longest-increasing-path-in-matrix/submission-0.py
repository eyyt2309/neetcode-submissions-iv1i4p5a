class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        ans = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):

                ans = max(ans, self.recurPath(matrix, row, col, memo))

        return ans
    def recurPath(self, matrix, row, col, memo):

        if memo[row][col] is not None:
            return memo[row][col]

        best = 1

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                if matrix[nr][nc] > matrix[row][col]:

                    best = max(best, 1 + self.recurPath(matrix, nr, nc, memo))

        memo[row][col] = best
        return best

