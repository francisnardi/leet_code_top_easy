# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


from typing import List


class Solution:
    def test_expected_nums(self) -> None:
        duplicate = True
        nums = [1, 2, 3, 1]
        assert duplicate == Solution.contains_duplicate(
            Solution, nums), "Lists should be equal."

    def contains_duplicate(self, nums: List[int]) -> bool:
        dic = {}
        for n in nums:
            if dic.pop(n, None) != None:
                return True
            dic[n] = 1
        return False


if __name__ == "__main__":
    Solution.test_expected_nums(Solution)
    print("OK. Lists are equal.")
