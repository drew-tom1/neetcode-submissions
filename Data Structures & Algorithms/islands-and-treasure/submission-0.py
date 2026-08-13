class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return grid
        
        queue = deque([])
        row_len, col_len = len(grid), len(grid[0])
        land = (2 ** 31) - 1
        curr_dist = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue.append((i,j))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                if grid[r][c] == land:
                    grid[r][c] = curr_dist

                if r + 1 < row_len and grid[r + 1][c] == land:
                    queue.append((r + 1, c))
                if c + 1 < col_len and grid[r][c + 1] == land:
                    queue.append((r, c + 1))
                if r > 0 and grid[r - 1][c] == land:
                    queue.append((r - 1, c))
                if c > 0 and grid[r][c - 1] == land:
                    queue.append((r, c - 1))
                    
            
            curr_dist += 1


        
        