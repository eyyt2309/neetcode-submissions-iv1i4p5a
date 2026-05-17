class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False

        def dfs(board, s, visited, idx, pos):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            if s == word:
                self.found = True
                return
            r, c = pos

            for direction in directions:
                dr, dc = direction
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                    if (nr, nc) not in visited and board[nr][nc] == word[idx]:
                        visited.append((nr, nc))
                        dfs(board, s+word[idx], visited, idx + 1, (nr, nc)) 
                        visited.pop()

        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    dfs(board, word[0], [(row, col)], 1, (row, col))

        return self.found
