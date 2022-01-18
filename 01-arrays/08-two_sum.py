# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List
import collections


class Solution:
    def test_expected_nums(self) -> None:
        target = 9
        nums = [2, 7, 11, 15]
        expected_nums = [0, 1]

        assert collections.Counter(expected_nums) == collections.Counter(
            Solution.two_sum(self, nums, target)), "Lists should be equal."

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] not in dic:
                dic[nums[i]] = i
            else:
                res = [dic[target-nums[i]], i]
                return res


if __name__ == "__main__":
    Solution.test_expected_nums(Solution)
    print("OK. Values are equal.")
