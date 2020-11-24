class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        i = 0
        cnt = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
                i += 1
            else:
                if not stack:
                    cnt += 1
                else:
                    stack.pop()

                if i + 1 >= len(s) or s[i + 1] != ')':
                    cnt += 1
                    i += 1
                    continue
                i += 2
        return cnt + len(stack) * 2