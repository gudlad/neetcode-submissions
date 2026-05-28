class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = collections.defaultdict(set)
        col_set = collections.defaultdict(set)
        box_set = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue

                if (num in row_set[row] or 
                    num in col_set[col] or 
                    num in box_set[(row//3, col//3)]): 
                    return False

                row_set[row].add(num)
                col_set[col].add(num)
                box_set[(row//3, col//3)].add(num)
        return True
                



