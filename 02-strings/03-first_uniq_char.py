# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def test_expected_nums(self) -> None:
        s = "leetcode"
        output = 0
        assert output == Solution.first_uniq_char(
            self, s), "Values should be equal."

    def first_uniq_char(self, s):
        count_map = {}
        for c in s:
            count_map[c] = count_map.get(c, 0) + 1
        for i, c in enumerate(s):
            if count_map[c] == 1:
                return i
        return -1


if __name__ == "__main__":
    Solution.test_expected_nums(Solution)
    print("OK. Values are equal.")
