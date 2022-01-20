# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

from typing import List
import numpy as np


class Solution:
    def test_expected_nums(self) -> None:
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        output = Solution.rotate_image(self, matrix)
        x = np.array(expected_output)
        y = np.array(output)
        assert x.all() == y.all(), "Values should be equal."

    def rotate_image(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        matrix.reverse()
        for x in range(n):
            for y in range(n-1, x-1, -1):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
        return matrix


if __name__ == "__main__":
    Solution.test_expected_nums(Solution)
    print("OK. Values are equal.")
