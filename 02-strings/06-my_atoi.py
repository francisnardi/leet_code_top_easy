# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

class Solution:
    def test_expected_nums(self) -> None:
        s = "   -42"
        output = -42
        assert output == Solution.my_atoi(
            self, s), "Values should be equal."

    def my_atoi(self, s: str) -> bool:
        ls = list(s.strip())
        if not ls:
            return 0
        sign = 1
        if ls[0] in ['-', '+']:
            if ls[0] == '-':
                sign = -1
            ls = ls[1:]
        res, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            res = res*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * res, 2**31-1))


if __name__ == "__main__":
    Solution.test_expected_nums(Solution)
    print("OK. Values are equal.")
