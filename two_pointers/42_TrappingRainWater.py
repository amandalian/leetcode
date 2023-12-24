"""
https://leetcode.com/problems/trapping-rain-water/submissions/1127299627
Runtime: 109 ms [Beats 76.83% of users with Python3]
Memory: 19.34 MB [Beats 6.12% of users with Python3]
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right = 0, 0
        p1, p2 = 0, len(height) - 1
        units = 0

        while p1 < p2:
            if height[p1] < height[p2]:
                if height[p1] > max_left:
                    max_left = height[p1]
                else:
                    units += max_left - height[p1]
                p1 += 1

            else:
                if height[p2] > max_right:
                    max_right = height[p2]
                else:
                    units += max_right - height[p2]
                p2 -= 1

            print(units)

        return units
