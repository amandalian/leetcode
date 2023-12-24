"""
https://leetcode.com/problems/container-with-most-water/submissions/1127265246
Runtime: 482 ms [Beats 99.50% of users with Python3]
Memory: 30.31 MB [Beats 5.02% of users with Python3]
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0  # from front
        p2 = len(height) - 1  # from back
        max_area = 0

        while p1 < p2:
            if height[p1] < height[p2]:
                max_area = max(max_area, (p2 - p1) * height[p1])
                p1 += 1
            else:
                max_area = max(max_area, (p2 - p1) * height[p2])
                p2 -= 1

        return max_area
