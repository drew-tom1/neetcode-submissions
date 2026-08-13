class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rl, cl = len(grid), len(grid[0])
        biggestIsland = 0
        visited = set()
        prevIslandSize = 0

        def dfs(r, c):
            if grid[r][c] == 1 and (r,c) not in visited:
                visited.add((r,c))
                print(r,c)
                if r >= 1:
                    dfs(r - 1, c)
                if r + 1 < rl:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < cl:
                    dfs(r, c + 1)
                print(count)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    dfs(i,j)
                    biggestIsland = max(biggestIsland, len(visited) - prevIslandSize)
                    prevIslandSize = len(visited)
        return biggestIsland
                    

            
   
        