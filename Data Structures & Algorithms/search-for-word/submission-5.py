class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        self.found = False

        self.visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c, s, pos):
            if s == word:
                self.found = True
                return True
            if pos >= len(word):
                return False
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for direction in directions:
                dr, dc = direction
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and self.visited[nr][nc] != True:
                    if board[nr][nc] == word[pos]:
                        new_s = s + word[pos]

                        self.visited[nr][nc] = True
                        if dfs(nr, nc, new_s, pos + 1):
                            return
                        self.visited[nr][nc] = False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    self.visited[row][col] = True
                    dfs(row, col, word[0], 1)
                    self.visited[row][col] = False

        return self.found
