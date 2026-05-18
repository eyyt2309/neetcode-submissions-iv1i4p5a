class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)]for _ in range(n)]
        self.ans = []
    
        def isSafe(row, col, board):
            # Check same column above
            for r in range(row):
                if board[r][col] == "Q":
                    return False

            # Check upper-left diagonal
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            # Check upper-right diagonal
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1

            return True

        def dfs(board, row, queens):
            if queens == n:
                self.ans.append(["".join(r) for r in board])
                return
            for col in range(n):
                if isSafe(row, col, board):
                    board[row][col] = 'Q'
                    dfs(board, row + 1, queens + 1)
                    board[row][col] = '.'
                

        dfs(board, 0, 0)

        return self.ans