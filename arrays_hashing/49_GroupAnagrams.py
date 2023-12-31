"""
https://leetcode.com/problems/group-anagrams/submissions/1127079454
Runtime: 91 ms [Beats 86.54% of users with Python3]
Memory: 20.16 MB [Beats 53.97% of users with Python3]
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        for s in strs:
            o = "".join(sorted(s))
            if o in mapper:
                mapper[o].append(s)
            else:
                mapper[o] = [s]

        return [mapper.get(o) for o in mapper]
