class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = set()
        atl = set()
        res = []

        def dfs(r, c, o):
            o.add((r,c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols 
                    and (nr, nc) not in o 
                    and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, o)

        for c in range(cols):
            dfs(0, c, pac)
            dfs(rows - 1, c, atl)

        for r in range(rows):
            dfs(r, 0, pac)
            dfs(r, cols - 1, atl)

        for i in range(rows):
            for j in range(cols):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        
        return res

            



        
        