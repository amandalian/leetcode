"""
https://leetcode.com/problems/product-of-array-except-self/submissions/1127102708
Runtime: 168 ms [Beats 98.26% of users with Python3]
Memory: 24.56 MB [Beats 32.85% of users with Python3]
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product, postfix_product = 1, 1
        result = len(nums) * [1]

        for i in range(len(nums) - 1):
            prefix_product *= nums[i]
            result[i + 1] *= prefix_product

        for i in range(len(nums) - 1, 0, -1):
            postfix_product *= nums[i]
            result[i - 1] *= postfix_product

        return result
