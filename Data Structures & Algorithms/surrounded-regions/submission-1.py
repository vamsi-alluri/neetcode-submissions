class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board:
            return

        # Start from borders, if islands are found, leave them as is and erase the board. 

        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        def dfs(i, j):            
            if i < 0 or j < 0 or i >= m or j >= n:
                return 

            if board[i][j] == 'O':
                board[i][j] = '0'
            else:
                return
            
            for dr, dc in directions:
                nr, nc = dr + i, dc + j
                dfs(nr, nc)
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == '0':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        return
