class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        empty = "."
        squares_map = defaultdict(set)


        for i in range(len(board)):

            row_set = set()
            col_set = set()
            
            for j in range(len(board[i])):

                box_id = (i // 3) * 3 + (j // 3)
                
                if board[i][j] != empty:
                    if board[i][j] in row_set or board[i][j] in squares_map[box_id]:
                        return False

                    row_set.add(board[i][j])
                    squares_map[box_id].add(board[i][j])
                    
                if board[j][i] != empty:
                    if board[j][i] in col_set:
                        return False
                    
                    col_set.add(board[j][i])
                
        return True
        