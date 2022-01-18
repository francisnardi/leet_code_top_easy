# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from typing import List
import collections


class Solution:
    def test_expected_nums(self) -> None:
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        output = True

        assert output == Solution.is_valid_sudoku(
            self, board), "Lists should be equal."

    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        final = set()
        l = len(board)

        for i in range(l):
            for j in range(l):
                temp = board[i][j]
                if temp != '.':
                    if (i, temp) in final or (temp, j) in final or (i//3, j//3, temp) in final:
                        return False
                    final.add((i, temp))
                    final.add((temp, j))
                    final.add((i//3, j//3, temp))
        return True


if __name__ == "__main__":
    Solution.test_expected_nums(Solution)
    print("OK. Values are equal.")
