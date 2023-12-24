"""
https://leetcode.com/problems/valid-sudoku/submissions/1127105975
Runtime: 94 ms [Beats 89.06% of users with Python3]
Memory: 17.45 MB [Beats 5.48% of users with Python3]
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            digits = set()
            for col in range(9):
                cell = board[row][col]
                if ord(cell) >= 49 and ord(cell) <= 57:
                    if cell not in digits:
                        digits.add(cell)
                    else:
                        return False

        for col in range(9):
            digits = set()
            for row in range(9):
                cell = board[row][col]
                if ord(cell) >= 49 and ord(cell) <= 57:
                    if cell not in digits:
                        digits.add(cell)
                    else:
                        return False

        for row_offset in [0, 3, 6]:
            for col_offset in [0, 3, 6]:
                digits = set()
                for row in range(3):
                    for col in range(3):
                        cell = board[row + row_offset][col + col_offset]
                        if ord(cell) >= 49 and ord(cell) <= 57:
                            if cell not in digits:
                                digits.add(cell)
                            else:
                                return False

        return True
