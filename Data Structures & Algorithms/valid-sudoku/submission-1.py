class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        # check rows
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    else:
                        row.add(board[i][j])
        

        # check cols
        for j in range (9):
            col = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in col:
                        return False
                    else:
                        col.add(board[i][j])


        # checks squares
        offsetx = 0 
        for x in range(3):
            offsety = 0
            for y in range(3):
                square = set()
                for i in range(3):
                    for j in range(3):
                        if board[i+offsetx][j+offsety] != ".":
                            if board[i+offsetx][j+offsety] in square:
                                return False
                            else:
                                square.add(board[offsetx+i][j+offsety])

                offsety += 3
            offsetx += 3
                    

        return True