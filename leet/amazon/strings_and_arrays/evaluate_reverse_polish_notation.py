import operator
import typing
List = typing.List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        #ops = {'*': operator.mul, '+': operator.add, '-': operator.sub, '/': operator.floordiv}
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }


        def helper(i):
            curop = tokens[i]
            first, j =  helper(i-1) if tokens[i-1] in "+-/*" else int(tokens[i-1]), i-1
            sec, j =  helper(j - 1) if tokens[j - 1] in "+-/*" else int(tokens[j - 1]), j
            return ops[curop](sec, first), j

        return helper(len(tokens) - 1)[0]


if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
