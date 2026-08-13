class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len, col_len = len(board), len(board[0])
        visited = set()

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or r >= row_len or c < 0 or c >= col_len or (r,c) in visited or board[r][c] != word[idx]:
                return False
            
            visited.add((r,c))

            res = (
                dfs(r + 1, c, idx + 1) or 
                dfs(r - 1, c, idx + 1) or 
                dfs(r, c + 1, idx + 1) or 
                dfs(r, c - 1, idx + 1)
                )

            visited.remove((r,c))

            return res
            
            

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, 0):
                    return True

        return False


        