# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

from typing import List


class Solution:
    def test_expected_nums(self) -> None:
        prices = [7, 1, 5, 3, 6, 4]
        expected_return = 7
        assert expected_return == Solution.max_profit(
            Solution, prices), "Values should be equal."

    def max_profit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(len(prices) - 1):
            maxprofit += max(prices[i+1] - prices[i], 0)
        return maxprofit


if __name__ == "__main__":
    Solution.test_expected_nums(Solution)
    print("OK. Values are equal.")
