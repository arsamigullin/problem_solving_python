class Solution(object):
    def checkValidString(self, s):
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0


class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star_stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == '*':
                star_stack.append(i)
            else:
                if not stack and not star_stack:
                    return False
                if stack:
                    stack.pop()
                else:
                    star_stack.pop()
        while stack and star_stack:
            if stack.pop()>star_stack.pop():
                return False
        return not stack


class Solution(object):
    def checkValidString(self, s):
        if not s: return True
        LEFTY, RIGHTY = '(*', ')*'

        n = len(s)
        dp = [[False] * n for _ in s]
        for i in range(n):
            if s[i] == '*':
                dp[i][i] = True
            if i < n-1 and s[i] in LEFTY and s[i+1] in RIGHTY:
                dp[i][i+1] = True

        for size in range(2, n):
            for i in range(n - size):
                if s[i] == '*' and dp[i+1][i+size]:
                    dp[i][i+size] = True
                elif s[i] in LEFTY:
                    for k in range(i+1, i+size+1):
                        if (s[k] in RIGHTY and
                                (k == i+1 or dp[i+1][k-1]) and
                                (k == i+size or dp[k+1][i+size])):
                            dp[i][i+size] = True

        return dp[0][-1]