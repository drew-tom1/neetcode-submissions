class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board) - 1, len(board[0]) - 1
        visited = set()

        def dfs(r, c):
            if r > rows or r < 0 or c > cols or c < 0:
                return
            if board[r][c] == "X":
                return
            if (r,c) in visited:
                return

            visited.add((r,c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[0][j] == "O":
                    dfs(0, j)
                if board[rows][j] == "O":
                    dfs(rows, j)
                if board[i][0] == "O":
                    dfs(i, 0)
                if board[i][cols] == "O":
                    dfs(i, cols)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"
        
        