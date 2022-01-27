# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def test_expected_nums(self) -> None:
        s = "anagram"
        t = "nagaram"
        output = True
        assert output == Solution.is_anagram(
            self, s, t), "Values should be equal."

    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set_s = set(s)
        for char in set_s:
            if s.count(char) != t.count(char):
                return False
        return True

if __name__ == "__main__":
    Solution.test_expected_nums(Solution)
    print("OK. Values are equal.")
