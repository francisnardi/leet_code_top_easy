# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

from typing import List
import collections


class Solution:
    def test_expected_nums(self) -> None:
        nums = [1, 1, 1, 3, 4, 5, 5, 5, 5, 7, 7, 7, 9, 9]
        expected_nums = [1, 3, 4, 5, 7, 9]
        returned_list = Solution.remove_duplicates(Solution, nums)
        assert collections.Counter(expected_nums) == collections.Counter(
            returned_list), "Values should be equal."

    def remove_duplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                del nums[i]
        return nums


if __name__ == "__main__":
    Solution.test_expected_nums(Solution)
    print("OK. Values are equal.")
