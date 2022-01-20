# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

from typing import List
import collections


class Solution:
    def test_expected_nums(self) -> None:
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        output1 = [4, 9]
        output2 = Solution.intersect(self, nums1, nums2)
        assert collections.Counter(output1) == collections.Counter(
            output2), "Values should be equal."

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ht1 = dict()
        ht2 = dict()
        intersection = []
        
        for num1 in nums1:
            ht1[num1] = ht1[num1] + 1 if num1 in ht1 else 1
            
        for num2 in nums2:
            ht2[num2] = ht2[num2] + 1 if num2 in ht2 else 1

        for key in ht2.keys():
            if key in ht1:
                intersection += key * [min([ht2[key],ht1[key]])]
            
        return intersection


if __name__ == "__main__":
    Solution.test_expected_nums(Solution)
    print("OK. Values are equal.")
