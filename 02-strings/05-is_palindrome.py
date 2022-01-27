# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def test_expected_nums(self) -> None:
        s = "A man, a plan, a canal: Panama"
        output = True
        assert output == Solution.is_palindrome(
            self, s), "Values should be equal."

    def is_palindrome(self, s: str) -> bool:
        x = [c for c in s if c.isalnum()]
        x = "".join(x).lower()
        s = x
        if (s == s[::-1]):
            return True
        return False


if __name__ == "__main__":
    Solution.test_expected_nums(Solution)
    print("OK. Values are equal.")
