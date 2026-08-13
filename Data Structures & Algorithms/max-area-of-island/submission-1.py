class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_len, col_len = len(grid), len(grid[0])
        res = 0
        visited = set()

        def dfs(r, c):
            if r >= row_len or c >= col_len or c < 0 or r < 0:
                return
            if (r,c) in visited:
                return
            if grid[r][c] == 1:
                visited.add((r,c))
                

                dfs(r + 1, c)
                dfs(r, c + 1)
                dfs(r - 1, c)
                dfs(r, c - 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                prev = len(visited)
                if grid[i][j] == 1 and (i, j) not in visited:
                    dfs(i, j)
                    res = max(res, len(visited) - prev)

        return res
                    