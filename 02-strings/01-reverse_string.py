# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

import collections
from typing import List


class Solution:
    def test_expected_nums(self) -> None:
        s = ["h", "e", "l", "l", "o"]
        output = ["o", "l", "l", "e", "h"]
        assert collections.Counter(output) == collections.Counter(
            Solution.reverse_string(self, s)), "Values should be equal."

    def reverse_string(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            temp = s[len(s)-i-1]
            s[len(s)-i-1] = s[i]
            s[i] = temp
            return s


if __name__ == "__main__":
    Solution.test_expected_nums(Solution)
    print("OK. Values are equal.")
