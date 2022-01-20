# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def test_expected_nums(self) -> None:
        x = 120
        output = 21
        assert output == Solution.reverse(self, x), "Values should be equal."

    def reverse(self, x: int) -> int:
        temp = int(str(abs(x))[::-1])
        if temp > 2147483647 or temp < -2147483648:
            return 0
        if (x > 0):
            return temp
        else:
            return -temp


if __name__ == "__main__":
    Solution.test_expected_nums(Solution)
    print("OK. Values are equal.")
