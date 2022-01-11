# Given an array, rotate the array to the right by k steps, where k is non-negative.

from typing import List


class Solution:
    def testExpectedNums():
        k = 3
        nums = [1, 2, 3, 4, 5, 6, 7]
        expectedNums = [5, 6, 7, 1, 2, 3, 4]
        assert expectedNums == Solution.rotate(
            Solution, nums, k), "Lists should be equal."

    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k % len(nums)):
            nums.insert(0, nums.pop())
        return nums


if __name__ == "__main__":
    Solution.testExpectedNums()
    print("OK. Lists are equal.")
