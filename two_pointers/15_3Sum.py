"""
https://leetcode.com/problems/3sum/submissions/1127263109
Runtime: 504 ms [Beats 99.05% of users with Python3]
Memory: 21.63 MB [Beats 8.00% of users with Python3]
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        if nums.count(0) >= 3:
            result.add((0, 0, 0))

        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]

        pos_set = set(pos)
        neg_set = set(neg)

        if nums.count(0) >= 1:
            for num in pos_set:
                if -num in neg_set:
                    result.add((0, num, -num))

        for i in range(len(pos) - 1):
            for j in range(i + 1, len(pos)):
                if -(pos[i] + pos[j]) in neg_set:
                    result.add(
                        (min(pos[i], pos[j]), max(pos[i], pos[j]), -(pos[i] + pos[j]))
                    )

        for i in range(len(neg) - 1):
            for j in range(i + 1, len(neg)):
                if -(neg[i] + neg[j]) in pos_set:
                    result.add(
                        (min(neg[i], neg[j]), max(neg[i], neg[j]), -(neg[i] + neg[j]))
                    )

        return list(result)
