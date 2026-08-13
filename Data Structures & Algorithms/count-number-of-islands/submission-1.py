class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0
        row_len, col_len = len(grid), len(grid[0])
        visited = set()
        land = "1"

        def dfs(r,c):
            if (r,c) not in visited and grid[r][c] == land:

                visited.add((r,c))
                
                # check boundaries before next recursive call
                if r + 1 < row_len:
                    dfs(r + 1, c)
                if r >= 1:
                    dfs(r - 1, c)
                if c + 1 < col_len:
                    dfs(r, c + 1)
                if c >= 1:
                    dfs(r, c - 1)
            
            

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == land:
                    dfs(i, j)
                    res += 1
        return res




            