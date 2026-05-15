class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = None   

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])

        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        res = []

        for row in range(rows):
            for col in range(cols):
                self.dfs(board, row, col, root, res)

        return res

    def dfs(self, board, row, col, node, res):

        ch = board[row][col]

        if ch not in node.children:
            return
        
        node = node.children[ch]

        if node.word is not None:
            res.append(node.word)
            node.word = None
        
        board[row][col] = '#'
        neighbors = self.getNeighbors(board, row, col, len(board),len(board[0]))

        for neighbor in neighbors:
            self.dfs(board, neighbor[0], neighbor[1], node, res)

        board[row][col] = ch


    def getNeighbors(self, board, r, c, rows, cols):
        neighbors = []
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for direction in directions:
            dr, dc = direction
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                neighbors.append((nr, nc))    

        return neighbors        
