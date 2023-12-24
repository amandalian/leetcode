"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1127330950
Runtime: 66 ms [Beats 88.59% of users with Python3]
Memory: 17.82 MB [Beats 5.64% of users with Python3]
"""

import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        ops = {"+", "-", "*", "/"}

        stack2 = []
        while True:
            p = len(tokens) - 1
            if tokens[p] in ops:
                if tokens[p - 1] not in ops:
                    if tokens[p - 2] not in ops:
                        op = tokens.pop()
                        n2 = int(tokens.pop())
                        n1 = int(tokens.pop())
                        if op == "+":
                            tokens.append(str(n1 + n2))
                        elif op == "-":
                            tokens.append(str(n1 - n2))
                        elif op == "*":
                            tokens.append(str(n1 * n2))
                        elif op == "/":
                            r = n1 / n2
                            if r > 0:
                                tokens.append(str(math.floor(r)))
                            else:
                                tokens.append(str(math.ceil(r)))

                        if len(stack2) > 0:
                            tokens.append(stack2.pop())
                            if tokens[-1] not in ops:
                                tokens.append(stack2.pop())
                        if len(tokens) == 1:
                            return int(tokens[0])

                    else:
                        stack2.append(tokens.pop())
                        stack2.append(tokens.pop())
                        continue
                else:
                    stack2.append(tokens.pop())
