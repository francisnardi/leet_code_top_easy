# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

from typing import List


class Solution:
    def test_expected_nums(self) -> None:
        duplicate = 2
        nums = [2, 3, 5, 4, 5, 3, 4]
        assert duplicate == Solution.single_number(
            Solution, nums), "Values should be equal."

    def single_number(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n
        return res


if __name__ == "__main__":
    Solution.test_expected_nums(Solution)
    print("OK. Values are equal.")
