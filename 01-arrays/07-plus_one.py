# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.


from typing import List
import collections


class Solution:
    def test_expected_nums(self) -> None:
        nums = [0, 1, 0, 3, 12]
        expected_nums = [1, 3, 12, 0, 0]

        assert collections.Counter(expected_nums) == collections.Counter(
            Solution.move_zeroes(self, nums)), "Values should be equal."

    def move_zeroes(self, nums: List[int]) -> List[int]:
        index = 0
        for item in range(len(nums)):
            if nums[item] != 0:
                temp = nums[item]
                nums[item] = nums[index]
                nums[index] = temp
                index += 1
        return nums


if __name__ == "__main__":
    Solution.test_expected_nums(Solution)
    print("OK. Values are equal.")
