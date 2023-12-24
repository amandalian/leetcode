"""
https://leetcode.com/problems/longest-consecutive-sequence/submissions/1127148395
Runtime: 511 ms [Beats 39.97% of users with Python3]
Memory: 55.74 MB [Beats 5.01% of users with Python3]
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        visited = {num: False for num in s}
        endpoints = {}
        longest = 0

        for num in s:
            if visited[num] == True:
                continue

            if (num - 1, 1) in endpoints and (num + 1, 0) in endpoints:
                start, end = endpoints[(num - 1, 1)], endpoints[(num + 1, 0)]
                endpoints[start], endpoints[end] = end, start
                endpoints.pop((num - 1, 1))
                endpoints.pop((num + 1, 0))
                longest = max(longest, end[0] - start[0] + 1)

            elif (num - 1, 1) in endpoints:
                start = endpoints[(num - 1, 1)]
                endpoints[start] = (num, 1)
                endpoints.pop((num - 1, 1))
                endpoints[(num, 1)] = start
                longest = max(longest, num - start[0] + 1)

            elif (num + 1, 0) in endpoints:
                end = endpoints[(num + 1, 0)]
                endpoints[end] = (num, 0)
                endpoints.pop((num + 1, 0))
                endpoints[(num, 0)] = end
                longest = max(longest, end[0] - num + 1)

            else:
                endpoints[(num, 0)] = (num, 1)
                endpoints[(num, 1)] = (num, 0)
                longest = max(longest, 1)

            visited[num] = True

        return longest
