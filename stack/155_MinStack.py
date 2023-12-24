"""
https://leetcode.com/problems/min-stack/submissions/1127314096
Runtime: 54 ms [Beats 89.62% of users with Python3]
Memory: 21.77 MB [Beats 5.73% of users with Python3]
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min = 2**31 - 1

    def push(self, val: int) -> None:
        self.stack.append((val, self.min))
        self.min = min(self.min, val)

    def pop(self) -> None:
        popped = self.stack.pop()
        self.min = popped[1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
