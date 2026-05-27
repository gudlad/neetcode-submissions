class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for row in range(9):
            row_set = set()
            for col in range(9):
                num = board[row][col]
                if num != ".":
                    if num in row_set:
                        return False
                    row_set.add(num)
        # col check
        for col in range(9):
            col_set = set()
            for row in range(9):
                num = board[row][col]
                if num != ".":
                    if num in col_set:
                        return False
                col_set.add(num)
        # box check
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_set = set()
                for row in range(box_row, box_row+3):
                    for col in range(box_col, box_col+3):
                        num = board[row][col]
                        if num !=".":
                            if num in box_set:
                                return False
                        box_set.add(num)
        return True


