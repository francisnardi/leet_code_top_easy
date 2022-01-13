# Given an array, rotate the array to the right by k steps, where k is non-negative.

from typing import List


class Solution:
    def test_expected_nums(self) -> None:
        k = 3
        nums = [1, 2, 3, 4, 5, 6, 7]
        expected_nums = [5, 6, 7, 1, 2, 3, 4]
        assert expected_nums == Solution.rotate(
            Solution, nums, k), "Lists should be equal."

    def rotate(self, nums: List[int], k: int) -> None:
        i = 0
        while(k % len(nums) - i > 0):
            nums.insert(0, nums.pop())
            i += 1
        return nums


if __name__ == "__main__":
    Solution.test_expected_nums(Solution)
    print("OK. Lists are equal.")
