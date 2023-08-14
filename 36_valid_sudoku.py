# Note:
    # A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    # Only the filled cells need to be validated according to the mentioned rules.

# Constraints:
    # board.length == 9
    # board[i].length == 9
    # board[i][j] is a digit 1-9 or '.'.


# Three different 'rules' the board needs to pass before being confirmed as a valid board.
    # Can create three different methods
        # Checking each ROW for duplicates
        # Checking each COLOUMN for duplicates
        # Checking each 3 x 3 BOX for duplicates
            # Could've sorted out each of the 3 x 3 boxes as an individual value in itself
            # E.g. Columns 0 - 2 and Row 0 - 2 could be ONE box (use of mod 3)


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        boardHeight = len(board)
        boardLength = len(board[1])
        # Constaints specify that the dimensions of the board is always 9x9 so no need for a board size checker

        # checking rows
        for singleList in board:
            # print(singleList)
            rowHash = {}
            for m in singleList:
                if m in rowHash:
                    print("Failed ROW check")
                    # return False
                elif m != ".":
                    rowHash[m] = 1

        # checking columns
        # I could make a new array for the numbers in the columns? This does take up a bit of extra memory and then requires another step after when looping through
        # Not sure of any other potential solutions
            # Maybe some while loop? board[i][j] and then iterate through?
        for i in range(0, boardHeight):
            columnHash = {}
            for j in range(0,boardLength):
                # print(board[j][i])
                for n in board[j][i]:
                    if n in columnHash:
                        print('Failed COLUMN check')
                        # return False
                    elif n != ".":
                        columnHash[n] = 1


        # checking grid
        # thought about this and its kinda rough
        # I've come up with some super skechty method to loop through boxes but it looks a lil hardcoded
        # I could do some array like [3, 6, 9] but that looks a lot more complicated?¿

        # First column of boxes
        x = 0
        boxHash = {}
        while x < 3:
            y = 0
                # print(board[x][y])
            while y < 3:
                if board[x][y] in boxHash:
                    print('Failed BOX check 1')
                    # return False
                elif board[x][y] != ".":
                    boxHash[board[x][y]] = 1
                y += 1
            x += 1

        boxHash = {}
        while x < 6:
            y = 0
                # print(board[x][y])
            while y < 3:
                if board[x][y] in boxHash:
                    print('Failed BOX check 2')
                    # return False
                elif board[x][y] != ".":
                    boxHash[board[x][y]] = 1
                y += 1
            x += 1

        boxHash = {}
        while x < 9:
            y = 0
                # print(board[x][y])
            while y < 3:
                if board[x][y] in boxHash:
                    print('Failed BOX check 3')
                    # return False
                elif board[x][y] != ".":
                    boxHash[board[x][y]] = 1
                y += 1
            x += 1

        # Second column of boxes
        x = 0
        boxHash = {}
        while x < 3:
            y = 3
                # print(board[x][y])
            while y < 6:
                if board[x][y] in boxHash:
                    print('Failed BOX check 4')
                    # return False
                elif board[x][y] != ".":
                    boxHash[board[x][y]] = 1
                y += 1
            x += 1

        boxHash = {}
        while x < 6:
            y = 3
                # print(board[x][y])
            while y < 6:
                if board[x][y] in boxHash:
                    print('Failed BOX check 5')
                    # return False
                elif board[x][y] != ".":
                    boxHash[board[x][y]] = 1
                y += 1
            x += 1

        boxHash = {}
        while x < 9:
            y = 3
                # print(board[x][y])
            while y < 6:
                if board[x][y] in boxHash:
                    print('Failed BOX check 6')
                    # return False
                elif board[x][y] != ".":
                    boxHash[board[x][y]] = 1
                y += 1
            x += 1


        # Third column of boxes
        x = 0
        boxHash = {}
        while x < 3:
            y = 6
            while y < 9:
                print(board[x][y])
                if board[x][y] in boxHash:
                    print('Failed BOX check 7')
                    # return False
                elif board[x][y] != ".":
                    boxHash[board[x][y]] = 1
                y += 1
            x += 1

        boxHash = {}
        while x < 6:
            y = 6
                # print(board[x][y])
            while y < 9:
                if board[x][y] in boxHash:
                    print('Failed BOX check 8')
                    # return False
                elif board[x][y] != ".":
                    boxHash[board[x][y]] = 1
                y += 1
            x += 1

        boxHash = {}
        while x < 9:
            y = 6
                # print(board[x][y])
            while y < 9:
                if board[x][y] in boxHash:
                    print('Failed BOX check 9')
                    # return False
                elif board[x][y] != ".":
                    boxHash[board[x][y]] = 1
                y += 1
            x += 1

        print("x")

        return board


board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
# >>> true


# board = [["8","3",".",".","7",".",".",".","."],
#          ["6",".",".","1","9","5",".",".","."],
#          [".","9","8",".",".",".",".","6","."],
#          ["8",".",".",".","6",".",".",".","3"],
#          ["4",".",".","8",".","3",".",".","1"],
#          ["7",".",".",".","2",".",".",".","6"],
#          [".","6",".",".",".",".","2","8","."],
#          [".",".",".","4","1","9",".",".","5"],
#          [".",".",".",".","8",".",".","7","9"]]
# >>> false

# board = [["8","3",".",".","7",".",".",".","."],
#          ["6",".",".","1","9","5",".",".","."],
#          [".","9","8",".",".",".",".","6","."],
#          ["2",".",".",".","6",".",".",".","3"],
#          ["4",".",".","8",".","3",".",".","1"],
#          ["7",".",".",".","2",".",".",".","6"],
#          [".","6",".",".",".",".","2","8","."],
#          [".",".",".","4","1","9",".",".","5"],
#          [".",".",".",".","8",".",".","7","9"]]
# >>> false

# board = [["5","3",".",".","7",".","5",".","."],["6",".",".","1","9","5",".",".","."]]
# fails row
# >>> false

# board = [["5","3",".",".","7",".",".",".","9"],["6",".",".","1","9","5",".",".","9"]]
# fails column
# >>> false

board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]
# >>> true

sol = Solution()
sol.isValidSudoku(board)
