"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1057689346
Runtime: 110 ms [Beats 91.92% of users with Python3]
Memory: 17.24 MB [Beats 47.81% of users with Python3]
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0  # from front
        p2 = len(numbers) - 1  # from back

        while p1 < p2:
            if numbers[p1] + numbers[p2] == target:
                break
            elif numbers[p1] + numbers[p2] > target:
                p2 -= 1
            else:
                p1 += 1

        return [p1 + 1, p2 + 1]
