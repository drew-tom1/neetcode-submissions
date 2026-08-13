class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rl, cl = len(grid), len(grid[0])
        ct = 0
        visited = set()

        def dfs(r, c):
            if grid[r][c] == "1" and (r,c) not in visited:
                visited.add((r,c))
                if r + 1 < rl:
                    dfs(r + 1,c)
                if r >= 1:
                    dfs(r - 1, c)
                if c + 1 < cl:
                    dfs(r, c + 1)
                if c >= 1:
                    dfs(r, c - 1)




        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    ct += 1

        return ct
        