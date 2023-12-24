"""
https://leetcode.com/problems/top-k-frequent-elements/submissions/1127084395
Runtime: 85 ms [Beats 97.48% of users with Python3]
Memory: 22.04 MB [Beats 10.19% of users with Python3]
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        return [i[0] for i in sorted(d.items(), key=lambda x: -x[1])[:k]]
