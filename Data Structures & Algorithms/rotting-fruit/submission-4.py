class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i,j))

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                if i + 1 < len(grid) and grid[i + 1][j] == 1:
                    grid[i+1][j] = 2
                    queue.append((i + 1,j))
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    grid[i-1][j] = 2
                    queue.append((i - 1, j))
                if j + 1 < len(grid[i]) and grid[i][j + 1] == 1:
                    grid[i][j+1] = 2
                    queue.append((i, j + 1))
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    grid[i][j-1] = 2
                    queue.append((i, j - 1))
            if queue:
                res += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        
        return res 

        
        
            
            
        