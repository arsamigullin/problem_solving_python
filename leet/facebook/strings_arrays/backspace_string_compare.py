import itertools


class MySolution:
    '''
    This is O(n) space complexity
    and O(n) complexity
    '''
    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(s):
            j = -1
            for i in range(len(s)):
                if s[i] == '#':
                    j = max(-1, j - 1)
                else:
                    j+=1
                    s[j]=s[i]
            return s[:j+1]
        return helper(list(S)) == helper(list(T))


# this is O(1) space complexity
# and O(n) complexity
class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0 # skip for imitating removing operation
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        def finalStr(s: str):
            stack = []
            for char in s:
                if stack and char == '#':
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return stack

        return finalStr(S) == finalStr(T)